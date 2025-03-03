import streamlit as stimport pandas as pdimport plotly.graph_objects as gofrom plotly.subplots import make_subplotsimport iofrom datetime import datetimefrom fpdf import FPDFimport smtplibfrom email.mime.text import MIMETextfrom email.mime.multipart import MIMEMultipartfrom email.mime.application import MIMEApplicationfrom utils.data_loader import calculate_metrics, get_expense_breakdownfrom utils.helpers import format_currencydef show_reports():    st.title("📋 Raporlar")    if 'data' not in st.session_state or st.session_state.data is None:        st.info("👆 Lütfen sol menüden bir veri dosyası yükleyin.")        return    data = st.session_state.data    # Rapor türü seçimi    report_type = st.selectbox(        "📊 Rapor Türü",        ["Özet Rapor", "Aylık Rapor", "Gider Raporu", "Detaylı Rapor"]    )    if report_type == "Özet Rapor":        show_summary_report(data)    elif report_type == "Aylık Rapor":        show_monthly_report(data)    elif report_type == "Gider Raporu":        show_expense_report(data)    else:        show_detailed_report(data)def show_summary_report(data):    """Özet rapor göster"""    st.subheader("📈 Finansal Özet")    metrics = calculate_metrics(data)    if metrics:        # Temel metrikler tablosu        summary_df = pd.DataFrame({            'Metrik': ['Toplam Satış', 'Toplam Gider', 'Net Kar', 'Kar Marjı'],            'Değer': [                format_currency(metrics['total_sales']),                format_currency(metrics['total_expenses']),                format_currency(metrics['profit']),                f"%{metrics['margin']:.2f}"            ]        })        st.dataframe(            summary_df,            hide_index=True,            use_container_width=True        )        # Grafikler        col1, col2 = st.columns(2)        with col1:            # Kar/Zarar grafiği            fig = go.Figure(data=[go.Bar(                x=['Satış', 'Gider', 'Kar'],                y=[metrics['total_sales'], metrics['total_expenses'], metrics['profit']],                marker_color=['#2ECC71', '#E74C3C', '#3498DB']            )])            fig.update_layout(                title="Finansal Genel Bakış",                height=400            )            st.plotly_chart(fig, use_container_width=True)        with col2:            # Dağılım pasta grafiği            fig = go.Figure(data=[go.Pie(                labels=['Satış', 'Gider', 'Kar'],                values=[metrics['total_sales'], metrics['total_expenses'], metrics['profit']],                hole=.3            )])            fig.update_layout(                title="Dağılım Analizi",                height=400            )            st.plotly_chart(fig, use_container_width=True)def show_monthly_report(data):    """Aylık rapor göster"""    st.subheader("📅 Aylık Performans Analizi")    metrics = calculate_metrics(data)    if metrics:        # Aylık trend grafiği        fig = make_subplots(rows=2, cols=1, subplot_titles=("Gelir ve Gider", "Kar ve Kar Marjı"))        months = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs',                  'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim'][:len(metrics['monthly_sales'])]        # Gelir ve Gider grafiği        fig.add_trace(            go.Bar(                name='Satış',                x=months,                y=metrics['monthly_sales'],                marker_color='#2ECC71'            ),            row=1, col=1        )        fig.add_trace(            go.Bar(                name='Gider',                x=months,                y=metrics['monthly_expenses'],                marker_color='#E74C3C'            ),            row=1, col=1        )        # Kar ve Kar Marjı grafiği        fig.add_trace(            go.Bar(                name='Kar',                x=months,                y=metrics['monthly_profits'],                marker_color='#3498DB'            ),            row=2, col=1        )        fig.add_trace(            go.Scatter(                name='Kar Marjı (%)',                x=months,                y=metrics['monthly_margins'],                line=dict(color='#E67E22', width=2),                yaxis='y2'            ),            row=2, col=1        )        fig.update_layout(height=800, showlegend=True)        fig.update_yaxes(title_text="%", secondary_y=True, row=2, col=1)        st.plotly_chart(fig, use_container_width=True)        # Aylık performans tablosu        monthly_df = pd.DataFrame({            'Ay': months,            'Satış': metrics['monthly_sales'],            'Gider': metrics['monthly_expenses'],            'Kar': metrics['monthly_profits'],            'Kar Marjı (%)': metrics['monthly_margins']        })        st.dataframe(            monthly_df,            column_config={                'Satış': st.column_config.NumberColumn('Satış', format="₺%d"),                'Gider': st.column_config.NumberColumn('Gider', format="₺%d"),                'Kar': st.column_config.NumberColumn('Kar', format="₺%d"),                'Kar Marjı (%)': st.column_config.ProgressColumn(                    'Kar Marjı (%)',                    format="%{value:.1f}%",                    min_value=0,                    max_value=100,                )            },            hide_index=True,            use_container_width=True        )def show_expense_report(data):    """Gider raporu göster"""    st.subheader("💰 Gider Analizi")    expense_data = get_expense_breakdown(data)    if expense_data is not None:        # Gider dağılım grafiği        fig = go.Figure()        # En yüksek 10 gider kalemi        top_expenses = expense_data.head(10)        fig.add_trace(go.Bar(            y=top_expenses['ESAS GİDER YERİ'],            x=top_expenses['Genel Toplam'],            orientation='h',            marker=dict(                color=top_expenses['Satış Oranı'],                colorscale='Viridis',                showscale=True,                colorbar=dict(title="Satış Oranı (%)")            ),            text=[f"₺{x:,.0f}<br>(%{y:.1f})" for x, y in                  zip(top_expenses['Genel Toplam'], top_expenses['Satış Oranı'])],            textposition='auto',        ))        fig.update_layout(            title="En Yüksek 10 Gider Kalemi",            height=500,            yaxis={'categoryorder': 'total ascending'},            xaxis_title="Tutar (TL)"        )        st.plotly_chart(fig, use_container_width=True)        # Gider tablosu        st.dataframe(            expense_data,            column_config={                'ESAS GİDER YERİ': st.column_config.TextColumn('Gider Kalemi'),                'Genel Toplam': st.column_config.NumberColumn('Toplam Tutar', format="₺%d"),                'ORTALAMA': st.column_config.NumberColumn('Aylık Ortalama', format="₺%d"),                'Satış Oranı': st.column_config.ProgressColumn(                    'Satış Oranı',                    format="%{value:.1f}%",                    min_value=0,                    max_value=100,                )            },            hide_index=True,            use_container_width=True        )def show_detailed_report(data):    """Detaylı rapor göster ve dışa aktarma seçenekleri sun"""    st.subheader("📊 Detaylı Finansal Rapor")    metrics = calculate_metrics(data)    expense_data = get_expense_breakdown(data)    if metrics and expense_data is not None:        # Excel için veriler        excel_dict = {            'Özet': pd.DataFrame({                'Metrik': ['Toplam Satış', 'Toplam Gider', 'Net Kar', 'Kar Marjı'],                'Değer': [                    format_currency(metrics['total_sales']),                    format_currency(metrics['total_expenses']),                    format_currency(metrics['profit']),                    f"%{metrics['margin']:.2f}"                ]            }),            'Aylık Performans': pd.DataFrame({                'Ay': ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs',                       'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim'][:len(metrics['monthly_sales'])],                'Satış': metrics['monthly_sales'],                'Gider': metrics['monthly_expenses'],                'Kar': metrics['monthly_profits'],                'Kar Marjı (%)': metrics['monthly_margins']            }),            'Gider Analizi': expense_data        }        col1, col2 = st.columns(2)        with col1:            # Excel raporu            excel_data = export_to_excel(excel_dict)            if excel_data:                st.download_button(                    label="📥 Excel Raporu İndir",                    data=excel_data,                    file_name=f"finansal_rapor_{datetime.now().strftime('%Y%m%d')}.xlsx",                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"                )        with col2:            # PDF raporu            pdf_data = create_pdf_report(excel_dict)            if pdf_data:                st.download_button(                    label="📥 PDF Raporu İndir",                    data=pdf_data,                    file_name=f"finansal_rapor_{datetime.now().strftime('%Y%m%d')}.pdf",                    mime="application/pdf"                )        # E-posta gönderme seçeneği        st.markdown("---")        st.subheader("📧 Raporu E-posta ile Gönder")        col1, col2 = st.columns(2)        with col1:            email = st.text_input("E-posta Adresi")        with col2:            report_format = st.selectbox(                "Rapor Formatı",                ["Excel", "PDF", "Her İkisi"]            )        if st.button("📤 Raporu Gönder"):            if email:                attachments = {}                if report_format in ["Excel", "Her İkisi"]:                    attachments[f"finansal_rapor_{datetime.now().strftime('%Y%m%d')}.xlsx"] = excel_data                if report_format in ["PDF", "Her İkisi"]:                    attachments[f"finansal_rapor_{datetime.now().strftime('%Y%m%d')}.pdf"] = pdf_data                if send_email_report(email, attachments):                    st.success("✅ Rapor başarıyla gönderildi!")                else:                    st.error("❌ Rapor gönderilirken bir hata oluştu!")            else:                st.warning("⚠️ Lütfen bir e-posta adresi girin!")def export_to_excel(df_dict):    """Excel dosyası oluştur"""    output = io.BytesIO()    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:        for sheet_name, df in df_dict.items():            df.to_excel(writer, sheet_name=sheet_name, index=False)    return output.getvalue()def create_pdf_report(df_dict):    """PDF raporu oluştur"""    try:        pdf = FPDF()        pdf.add_page()        # Başlık        pdf.set_font("Arial", "B", 16)        pdf.cell(0, 10, "Finansal Rapor", ln=True, align='C')        pdf.ln(10)        # Her DataFrame için tablo oluştur        for sheet_name, df in df_dict.items():            pdf.set_font("Arial", "B", 12)            pdf.cell(0, 10, sheet_name, ln=True)            pdf.ln(5)            pdf.set_font("Arial", "B", 10)            for col in df.columns:                pdf.cell(40, 10, str(col), 1)            pdf.ln()            pdf.set_font("Arial", "", 10)            for _, row in df.iterrows():                for item in row:                    pdf.cell(40, 10, str(item), 1)                pdf.ln()            pdf.ln(10)        return pdf.output(dest='S').encode('latin1')    except Exception as e:        st.error(f"PDF oluşturma hatası: {str(e)}")        return Noneif __name__ == "__main__":    show_reports()