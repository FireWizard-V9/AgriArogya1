import streamlit as st
import plotly.express as px
import pandas as pd
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Define the app function
def app():
    # Subheader and custom padding at the top
    st.subheader(":bar_chart: Crops in India and Diseases")
    st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

    # Load the dataset
    df = pd.read_csv('crop_disease_data.csv', encoding='ISO-8859-1')

    # Sidebar filters
    st.sidebar.header("Choose your filter:")
    region = st.sidebar.multiselect("Region", df["Region"].unique())
    state = st.sidebar.multiselect("State", df[df["Region"].isin(region)]["State"].unique() if region else df["State"].unique())
    crop = st.sidebar.multiselect("Crop Type", df[df["State"].isin(state)]["Crop Type"].unique() if state else df["Crop Type"].unique())
    disease = st.sidebar.multiselect("Disease", df[df["Crop Type"].isin(crop)]["Disease"].unique() if crop else df["Disease"].unique())

    # Apply filters
    filtered_df = df.copy()
    if region:
        filtered_df = filtered_df[filtered_df["Region"].isin(region)]
    if state:
        filtered_df = filtered_df[filtered_df["State"].isin(state)]
    if crop:
        filtered_df = filtered_df[filtered_df["Crop Type"].isin(crop)]
    if disease:
        filtered_df = filtered_df[filtered_df["Disease"].isin(disease)]

    # Visualization columns
    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(filtered_df, x='Crop Type', y='Total Yield in a Year (tons/ha)', title='Cropwise Yield In a Year')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.pie(filtered_df, names='Crop Type', title='Diseases by Crop Type', hole=0.5)
        fig2.update_traces(textposition='outside')
        st.plotly_chart(fig2, use_container_width=True)

    # Expandable data view with download option
    with st.expander("View Data"):
        st.write(filtered_df.style.background_gradient(cmap="BrBG"))
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(label="Download Data", data=csv, file_name="Filtered_Data.csv", mime="text/csv")

    # Additional visualizations
    st.plotly_chart(px.bar(filtered_df, x='Region', y='Disease', color='Disease', title='Top Diseases by Region', barmode='stack'), use_container_width=True)

    # Correlation heatmap
    corr = filtered_df[['Max Temp (°C)', 'Min Temp (°C)', 'Relative Humidity (%)', 
                        'Rainfall (mm)', 'Wind Speed (kmph)', 'Total Yield in a Year (tons/ha)']].corr()

    st.plotly_chart(px.imshow(corr, text_auto=True, title='Correlation Heatmap of Environmental Factors'), use_container_width=True)

    # Scatter plots
    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(px.scatter(filtered_df, x='Rainfall (mm)', y='Total Yield in a Year (tons/ha)', color='Crop Type', 
                                   title='Rainfall vs. Crop Yield', hover_data=['Region', 'State']), use_container_width=True)
    with col4:
        st.plotly_chart(px.scatter(filtered_df, x='Max Temp (°C)', y='Total Yield in a Year (tons/ha)', color='Crop Type', 
                                   title='Max Temperature vs. Crop Yield', hover_data=['Region', 'State']), use_container_width=True)

    # Sunburst and line plots
    col5, col6 = st.columns(2)
    with col5:
        st.plotly_chart(px.sunburst(filtered_df, path=['Region', 'State', 'Crop Type', 'Disease'], values='Total Yield in a Year (tons/ha)', 
                                    title='Hierarchical View of Crop Data by Region and State'), use_container_width=True)
    with col6:
        st.plotly_chart(px.line(filtered_df, x='Season', y='Total Yield in a Year (tons/ha)', color='Crop Type', 
                                title='Seasonal Yield Trends by Crop Type', markers=True), use_container_width=True)

    # Treemap visualization
    st.plotly_chart(px.treemap(filtered_df, path=['Soil Requirements', 'Water Requirement', 'Crop Type'], 
                               values='Total Yield in a Year (tons/ha)', title='Soil and Water Requirements by Crop Type'), use_container_width=True)

    # Disease details dataframe
    st.markdown("#### **Disease Details**")
    st.dataframe(filtered_df[['Disease', 'Pathogens', 'Recommended Practices', 'Treatments']])
