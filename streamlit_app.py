import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Sandeep's AI Wealth Management",
    page_icon="🧠",
    layout="wide"
)

def main():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 10px; color: white; text-align: center; margin-bottom: 
2rem;'>
        <h1>🧠 AI Wealth Management</h1>
        <p>Intelligent Investment Strategies for Indian Markets</p>
        <p><strong>By Sandeep Yadav</strong> | Advanced AI-Powered Financial Planning</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("🎉 Your AI Wealth Management System is Running!")
    st.info("This is demo mode. Configure API keys for full functionality.")
    
    tab1, tab2, tab3 = st.tabs(["🤖 AI Assistant", "📊 Market Data", "🎯 Portfolio Planner"])
    
    with tab1:
        st.markdown("### 🤖 Your AI Financial Advisor")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📈 Analyze HDFC Bank"):
                st.markdown("""
                **📈 HDFC Bank Stock Analysis**
                
                **Current Status:** ₹1,589 (+0.8%)
                
                **✅ Strengths:**
                - Leading private bank with 35+ year track record
                - Strong digital banking platform
                - Consistent dividend payments
                
                **📊 Key Metrics:**
                - P/E Ratio: 18.5x (reasonable for banking)
                - ROE: 16.8% (industry-leading)
                - Net Interest Margin: 4.2%
                
                **🎯 Recommendation:** BUY for long-term (3+ years)
                **Risk Level:** Moderate
                **Portfolio Allocation:** 5-8% of equity portion
                
                *Demo analysis - Configure API keys for real-time AI insights*
                """)
        
        with col2:
            if st.button("💰 SIP Strategy"):
                st.markdown("""
                **💰 Smart SIP Strategy for ₹20,000/month**
                
                **🎯 Recommended Allocation:**
                
                **🔵 Large Cap (40% - ₹8,000)**
                - HDFC Top 100 Fund
                - Expected: 10-12% annually
                
                **🟢 Multi Cap (30% - ₹6,000)**  
                - Parag Parikh Flexi Cap Fund
                - Expected: 12-15% annually
                
                **🏛️ ELSS (20% - ₹4,000)**
                - Axis Long Term Equity Fund
                - Tax Benefit: ₹48,000 annual deduction
                
                **🌍 International (10% - ₹2,000)**
                - Motilal Oswal Nasdaq 100
                - Currency diversification
                
                **📈 Projected Wealth (12% CAGR):**
                - 10 Years: ₹46L (Investment: ₹24L)
                - 15 Years: ₹99L (Investment: ₹36L)
                
                *Demo strategy - Real AI provides personalized plans*
                """)
        
        with col3:
            if st.button("🏛️ Tax Planning"):
                st.markdown("""
                **🏛️ Tax-Saving Guide 2024-25**
                
                **💰 Section 80C (₹1.5L limit):**
                
                **🥇 ELSS Mutual Funds (Best Option)**
                - Investment: ₹1,50,000 annually
                - Lock-in: Only 3 years
                - Expected Return: 12-15%
                - Tax Saving: ₹46,500 (30% rate)
                
                **🏛️ Section 80CCD(1B) (₹50K extra):**
                - NPS investment
                - Additional ₹15,000 tax saving
                
                **💊 Section 80D (Health Insurance):**
                - Self + Family: ₹25,000
                - Parents >60: ₹50,000
                
                **🎯 Total Tax Saving Potential:**
                - 80C: ₹46,500
                - 80CCD(1B): ₹15,000  
                - 80D: ₹22,500
                - **Total: ₹84,000+ annually**
                
                *Demo guide - AI provides personalized strategies*
                """)
        
        query = st.text_input("Ask about investments:")
        if query:
            st.markdown(f"""
            **🤖 Demo Response to: "{query}"**
            
            In full mode, you would get:
            ✅ Real-time market analysis
            ✅ Personalized recommendations  
            ✅ Tax optimization strategies
            ✅ Goal-based planning
            
            *Configure API keys for advanced AI responses*
            """)
    
    with tab2:
        st.markdown("### 📊 Indian Market Dashboard")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("NIFTY 50", "19,845", "+125 (0.64%)")
        with col2:
            st.metric("SENSEX", "66,590", "+234 (0.35%)")
        with col3:
            st.metric("BANK NIFTY", "45,235", "-89 (-0.20%)")
        with col4:
            st.metric("NIFTY IT", "29,876", "+157 (0.53%)")
        
        st.markdown("#### 📈 NIFTY 50 Performance")
        dates = pd.date_range(start='2024-02-21', end='2024-08-21', freq='D')
        prices = 19000 + np.cumsum(np.random.normal(0, 50, len(dates)))
        
        chart_data = pd.DataFrame({'Date': dates, 'NIFTY 50': prices})
        fig = px.line(chart_data, x='Date', y='NIFTY 50', title='NIFTY 50 - 6 Month Chart')
        fig.update_traces(line_color='#667eea', line_width=2)
        st.plotly_chart(fig, use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🔥 Top Gainers")
            gainers = pd.DataFrame({
                'Stock': ['RELIANCE', 'TCS', 'HDFC BANK'],
                'Price': [2485, 3654, 1590],
                'Change (%)': [2.3, 1.8, 1.2]
            })
            st.dataframe(gainers)
        
        with col2:
            st.markdown("#### 📊 Market Sentiment")
            st.markdown("""
            **🟢 Positive Sectors:**
            - Banking (+1.2%)
            - IT Services (+0.8%)
            
            **🔴 Negative Sectors:**
            - Pharma (-0.5%)
            - FMCG (-0.3%)
            """)
    
    with tab3:
        st.markdown("### 🎯 Portfolio Planner")
        
        col1, col2 = st.columns(2)
        with col1:
            age = st.slider("Age", 18, 65, 30)
            income = st.number_input("Monthly Income (₹)", 20000, 1000000, 75000)
        with col2:
            expenses = st.number_input("Monthly Expenses (₹)", 10000, 500000, 45000)
            risk = st.selectbox("Risk Appetite", ["Conservative", "Moderate", "Aggressive"])
        
        surplus = income - expenses
        if surplus > 0:
            st.success(f"💰 Investable Surplus: ₹{surplus:,}/month")
            
            if st.button("🧠 Generate Strategy"):
                equity_pct = 40 if risk == "Conservative" else 60 if risk == "Moderate" else 80
                equity_amount = int(surplus * equity_pct / 100)
                debt_amount = surplus - equity_amount
                
                st.markdown(f"""
                ### 🎯 Recommended Portfolio
                
                **Monthly Investment:** ₹{surplus:,}
                - **Equity ({equity_pct}%):** ₹{equity_amount:,}
                - **Debt ({100-equity_pct}%):** ₹{debt_amount:,}
                
                **Expected Returns:** 12-14% annually
                **10-Year Corpus:** ₹{surplus * 12 * 10 * 2:,}
                
                **Fund Recommendations:**
                - Large Cap: HDFC Top 100 Fund
                - Multi Cap: Parag Parikh Flexi Cap
                - ELSS: Axis Long Term Equity
                """)
        else:
            st.warning("⚠️ No investable surplus detected.")
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 1rem; background: #667eea; color: white; border-radius: 
10px;'>
        <strong>Created by Sandeep Yadav</strong><br>
        🌐 <a href="https://sandeepyadav.co.in" style="color: white;">sandeepyadav.co.in</a> | 
        📧 <a href="mailto:contact@sandeepyadav.co.in" style="color: 
white;">contact@sandeepyadav.co.in</a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
