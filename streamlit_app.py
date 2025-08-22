import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from anthropic import Anthropic
import yfinance as yf

st.set_page_config(
    page_title="Sandeep's AI Wealth Management",
    page_icon="🧠",
    layout="wide"
)

# Initialize AI client with error handling
def get_ai_client():
    try:
        claude_api_key = st.secrets.get("CLAUDE_API_KEY", "demo-key")
        if claude_api_key and claude_api_key != "demo-key" and claude_api_key.startswith("sk-ant-"):
            return Anthropic(api_key=claude_api_key)
    except Exception as e:
        st.error(f"Failed to initialize AI client: {str(e)}")
    return None

def get_ai_response(prompt, client):
    if client is None:
        return "Demo mode: Configure Claude API key in Streamlit Cloud secrets for real AI responses."
    
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"

def get_stock_data(symbol):
    try:
        stock = yf.Ticker(f"{symbol}.NS")  # .NS for NSE stocks
        info = stock.info
        hist = stock.history(period="1d")
        if not hist.empty:
            current_price = hist['Close'].iloc[-1]
            return {
                'price': current_price,
                'company': info.get('longName', symbol),
                'market_cap': info.get('marketCap', 'N/A'),
                'pe_ratio': info.get('trailingPE', 'N/A')
            }
    except:
        pass
    return None

def main():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 10px; color: white; text-align: center; margin-bottom: 2rem;'>
        <h1>🧠 AI Wealth Management</h1>
        <p>Intelligent Investment Strategies for Indian Markets</p>
        <p><strong>By Sandeep Yadav</strong> | Advanced AI-Powered Financial Planning</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Check API status
    client = get_ai_client()
    if client:
        st.success("✅ AI System Active - Real-time Analysis Available")
    else:
        st.info("ℹ️ Demo Mode - Configure API keys for full functionality")
    
    tab1, tab2, tab3 = st.tabs(["🤖 AI Assistant", "📊 Market Data", "🎯 Portfolio Planner"])
    
    with tab1:
        st.markdown("### 🤖 Your AI Financial Advisor")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📈 Analyze HDFC Bank"):
                with st.spinner("Analyzing HDFC Bank..."):
                    stock_data = get_stock_data("HDFCBANK")
                    
                    if client and stock_data:
                        prompt = f"""Analyze HDFC Bank stock for Indian investors. Current price: ₹{stock_data['price']:.2f}, 
                        PE Ratio: {stock_data['pe_ratio']}, Market Cap: {stock_data['market_cap']}.
                        Provide: 1) Current analysis 2) Investment recommendation 3) Risk assessment 4) Price targets.
                        Keep response under 300 words, use Indian context."""
                        
                        response = get_ai_response(prompt, client)
                        st.markdown(f"**📈 HDFC Bank AI Analysis**\n\n{response}")
                    else:
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
                with st.spinner("Generating SIP strategy..."):
                    if client:
                        prompt = """Create a detailed SIP strategy for ₹20,000/month investment for Indian investors.
                        Include: 1) Asset allocation 2) Specific fund recommendations 3) Expected returns 4) Tax benefits
                        5) 10-year wealth projection. Focus on Indian mutual funds and tax-saving options."""
                        
                        response = get_ai_response(prompt, client)
                        st.markdown(f"**💰 AI-Generated SIP Strategy**\n\n{response}")
                    else:
                        st.markdown("""
                        **💰 Smart SIP Strategy for ₹20,000/month**
                        
                        **🎯 Recommended Allocation:**
                        
                        **🔵 Large Cap (40% - ₹8,000)**
                        - HDFC Top 100 Fund
                        - Expected: 10-12% annually
                        
                        **🟢 Multi Cap (30% - ₹6,000)**  
                        - Parag Parikh Flexi Cap Fund
                        - Expected: 12-15% annually
                        
                        **🛡️ ELSS (20% - ₹4,000)**
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
            if st.button("🛡️ Tax Planning"):
                with st.spinner("Analyzing tax-saving options..."):
                    if client:
                        prompt = """Provide comprehensive tax planning guide for Indian investors for FY 2024-25.
                        Include: 1) Section 80C options 2) ELSS vs other instruments 3) Section 80D health insurance
                        4) NPS benefits 5) Total tax saving calculation. Be specific with amounts and tax rates."""
                        
                        response = get_ai_response(prompt, client)
                        st.markdown(f"**🛡️ AI Tax Planning Guide**\n\n{response}")
                    else:
                        st.markdown("""
                        **🛡️ Tax-Saving Guide 2024-25**
                        
                        **💰 Section 80C (₹1.5L limit):**
                        
                        **🥇 ELSS Mutual Funds (Best Option)**
                        - Investment: ₹1,50,000 annually
                        - Lock-in: Only 3 years
                        - Expected Return: 12-15%
                        - Tax Saving: ₹46,500 (30% rate)
                        
                        **🛡️ Section 80CCD(1B) (₹50K extra):**
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
        
        st.markdown("#### 💬 Ask Your AI Advisor")
        query = st.text_input("Ask about investments, stocks, mutual funds, or financial planning:")
        
        if query:
            with st.spinner("AI is analyzing your query..."):
                if client:
                    prompt = f"""You are an expert Indian financial advisor. Answer this investment question: "{query}"
                    
                    Provide practical advice considering:
                    - Indian market context
                    - Tax implications
                    - Risk factors
                    - Specific recommendations
                    
                    Keep response under 300 words and actionable."""
                    
                    response = get_ai_response(prompt, client)
                    st.markdown(f"**🤖 AI Financial Advisor Response:**\n\n{response}")
                else:
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
        
        # Get real market data
        with st.spinner("Loading real market data..."):
            try:
                # Fetch major indices
                nifty = yf.Ticker("^NSEI")
                sensex = yf.Ticker("^BSESN")
                banknifty = yf.Ticker("^NSEBANK")
                
                # Get current day data
                nifty_data = nifty.history(period="2d")
                sensex_data = sensex.history(period="2d")
                banknifty_data = banknifty.history(period="2d")
                
                if not nifty_data.empty and len(nifty_data) >= 2:
                    nifty_current = nifty_data['Close'].iloc[-1]
                    nifty_prev = nifty_data['Close'].iloc[-2]
                    nifty_change = nifty_current - nifty_prev
                    nifty_pct = (nifty_change / nifty_prev) * 100
                else:
                    nifty_current, nifty_change, nifty_pct = 19845, 125, 0.64
                
                if not sensex_data.empty and len(sensex_data) >= 2:
                    sensex_current = sensex_data['Close'].iloc[-1]
                    sensex_prev = sensex_data['Close'].iloc[-2]
                    sensex_change = sensex_current - sensex_prev
                    sensex_pct = (sensex_change / sensex_prev) * 100
                else:
                    sensex_current, sensex_change, sensex_pct = 66590, 234, 0.35
                
                if not banknifty_data.empty and len(banknifty_data) >= 2:
                    banknifty_current = banknifty_data['Close'].iloc[-1]
                    banknifty_prev = banknifty_data['Close'].iloc[-2]
                    banknifty_change = banknifty_current - banknifty_prev
                    banknifty_pct = (banknifty_change / banknifty_prev) * 100
                else:
                    banknifty_current, banknifty_change, banknifty_pct = 45235, -89, -0.20
                
            except Exception as e:
                st.warning(f"Unable to fetch live data: {str(e)}. Showing sample data.")
                nifty_current, nifty_change, nifty_pct = 19845, 125, 0.64
                sensex_current, sensex_change, sensex_pct = 66590, 234, 0.35
                banknifty_current, banknifty_change, banknifty_pct = 45235, -89, -0.20
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("NIFTY 50", f"{nifty_current:,.0f}", f"{nifty_change:+.0f} ({nifty_pct:+.2f}%)")
        with col2:
            st.metric("SENSEX", f"{sensex_current:,.0f}", f"{sensex_change:+.0f} ({sensex_pct:+.2f}%)")
        with col3:
            st.metric("BANK NIFTY", f"{banknifty_current:,.0f}", f"{banknifty_change:+.0f} ({banknifty_pct:+.2f}%)")
        with col4:
            # Fetch NIFTY IT
            try:
                niftyit = yf.Ticker("^CNXIT")
                niftyit_data = niftyit.history(period="2d")
                if not niftyit_data.empty and len(niftyit_data) >= 2:
                    niftyit_current = niftyit_data['Close'].iloc[-1]
                    niftyit_prev = niftyit_data['Close'].iloc[-2]
                    niftyit_change = niftyit_current - niftyit_prev
                    niftyit_pct = (niftyit_change / niftyit_prev) * 100
                    st.metric("NIFTY IT", f"{niftyit_current:,.0f}", f"{niftyit_change:+.0f} ({niftyit_pct:+.2f}%)")
                else:
                    st.metric("NIFTY IT", "29,876", "+157 (0.53%)")
            except:
                st.metric("NIFTY IT", "29,876", "+157 (0.53%)")
        
        st.markdown("#### 📈 NIFTY 50 Performance (6 Months)")
        
        # Get real NIFTY historical data
        try:
            nifty_hist = nifty.history(period="6mo")
            if not nifty_hist.empty:
                chart_data = pd.DataFrame({
                    'Date': nifty_hist.index,
                    'NIFTY 50': nifty_hist['Close']
                })
                fig = px.line(chart_data, x='Date', y='NIFTY 50', title='NIFTY 50 - Real 6 Month Chart')
                fig.update_traces(line_color='#667eea', line_width=2)
                fig.update_layout(
                    xaxis_title="Date",
                    yaxis_title="Price",
                    showlegend=False
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error("Unable to load historical data")
        except Exception as e:
            st.error(f"Error loading chart data: {str(e)}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🔥 Top Gainers")
            try:
                # Get real stock data for major Indian stocks
                stocks = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS']
                gainers_data = []
                
                for stock in stocks:
                    try:
                        ticker = yf.Ticker(stock)
                        data = ticker.history(period="2d")
                        if not data.empty and len(data) >= 2:
                            current = data['Close'].iloc[-1]
                            prev = data['Close'].iloc[-2]
                            change_pct = ((current - prev) / prev) * 100
                            gainers_data.append({
                                'Stock': stock.replace('.NS', ''),
                                'Price': f"₹{current:.0f}",
                                'Change (%)': f"{change_pct:+.2f}%"
                            })
                    except:
                        continue
                
                if gainers_data:
                    # Sort by change percentage and take top 3
                    gainers_data.sort(key=lambda x: float(x['Change (%)'].replace('%', '').replace('+', '')), reverse=True)
                    gainers_df = pd.DataFrame(gainers_data[:3])
                    st.dataframe(gainers_df, hide_index=True)
                else:
                    # Fallback to static data
                    gainers = pd.DataFrame({
                        'Stock': ['RELIANCE', 'TCS', 'HDFC BANK'],
                        'Price': ['₹2,485', '₹3,654', '₹1,590'],
                        'Change (%)': ['+2.3%', '+1.8%', '+1.2%']
                    })
                    st.dataframe(gainers, hide_index=True)
                    st.caption("Sample data - Real-time data unavailable")
                    
            except Exception as e:
                # Fallback to static data
                gainers = pd.DataFrame({
                    'Stock': ['RELIANCE', 'TCS', 'HDFC BANK'],
                    'Price': ['₹2,485', '₹3,654', '₹1,590'],
                    'Change (%)': ['+2.3%', '+1.8%', '+1.2%']
                })
                st.dataframe(gainers, hide_index=True)
                st.caption("Sample data - Real-time data unavailable")
        
        with col2:
            st.markdown("#### 📊 Market Sentiment")
            try:
                # Calculate sector performance based on real data
                sectors = {
                    'Banking': banknifty_pct,
                    'IT Services': niftyit_pct if 'niftyit_pct' in locals() else 0.8,
                    'Pharma': -0.5,  # Would need additional API calls for these
                    'FMCG': -0.3
                }
                
                positive_sectors = [(k, v) for k, v in sectors.items() if v > 0]
                negative_sectors = [(k, v) for k, v in sectors.items() if v < 0]
                
                sentiment_text = "**🟢 Positive Sectors:**\n"
                for sector, pct in positive_sectors:
                    sentiment_text += f"- {sector} ({pct:+.1f}%)\n"
                
                sentiment_text += "\n**🔴 Negative Sectors:**\n"
                for sector, pct in negative_sectors:
                    sentiment_text += f"- {sector} ({pct:+.1f}%)\n"
                
                st.markdown(sentiment_text)
                
            except:
                st.markdown("""
                **🟢 Positive Sectors:**
                - Banking (+1.2%)
                - IT Services (+0.8%)
                
                **🔴 Negative Sectors:**
                - Pharma (-0.5%)
                - FMCG (-0.3%)
                """)
                st.caption("Sample data - Real-time sector data unavailable")
    
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
            
            if st.button("🧠 Generate AI Strategy"):
                with st.spinner("AI is creating your personalized strategy..."):
                    if client:
                        prompt = f"""Create a personalized investment strategy for:
                        - Age: {age}
                        - Monthly Income: ₹{income:,}
                        - Monthly Expenses: ₹{expenses:,}
                        - Surplus: ₹{surplus:,}
                        - Risk Appetite: {risk}
                        
                        Provide:
                        1) Asset allocation strategy
                        2) Specific mutual fund recommendations
                        3) Expected returns and time horizon
                        4) Tax optimization
                        5) 10-year wealth projection
                        
                        Consider Indian market context and regulations."""
                        
                        response = get_ai_response(prompt, client)
                        st.markdown(f"**🎯 AI-Generated Portfolio Strategy**\n\n{response}")
                    else:
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
                        
                        *Demo strategy - Configure API keys for personalized AI analysis*
                        """)
        else:
            st.warning("⚠️ No investable surplus detected.")
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 1rem; background: #667eea; color: white; border-radius: 10px;'>
        <strong>Created by Sandeep Yadav</strong><br>
        🌐 <a href="https://sandeepyadav.co.in" style="color: white;">sandeepyadav.co.in</a> | 
        📧 <a href="mailto:contact@sandeepyadav.co.in" style="color: white;">contact@sandeepyadav.co.in</a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()