# 📊 Data Visualization Facilitator

A user-friendly **Streamlit web application** that makes data visualization accessible to everyone. Upload your data, create beautiful interactive charts, and build comprehensive reports without any coding knowledge required.

## ✨ Features

### 🏠 **Home Page**
- **File Upload**: Support for CSV, XLS, and XLSX files
- **Data Preview**: Interactive data editor to modify your dataset
- **Project Naming**: Add custom titles to your visualization projects

### 📈 **Visualization Tools**
- **Line Charts**: Perfect for showing trends over time
- **Bar Charts**: Great for comparing categories
- **Scatter Plots**: Ideal for exploring relationships between variables
- **Pie Charts**: Excellent for showing proportions
- **Box Plots**: Statistical distribution visualization
- **Histograms**: Frequency distribution analysis

### 😎 **Results Dashboard**
- **Chart Collection**: Save and organize multiple visualizations
- **Report Generation**: View all your charts in a consolidated dashboard
- **Custom Styling**: Professional-looking reports with your project title

### 📧 **Contact Page**
- Simple contact form for user feedback and support

## 🚀 Quick Start

### Prerequisites
Make sure you have Python 3.7+ installed on your system.

### Installation
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Data-visualization-
   ```

2. **Install required packages**
   ```bash
   pip install streamlit pandas plotly streamlit-option-menu pillow openpyxl
   ```

3. **Run the application**
   ```bash
   streamlit run 🏠️_Home.py
   ```

4. **Open in browser**
   The application will automatically open in your default browser at `http://localhost:8501`

## 📖 How to Use

### Step 1: Upload Your Data
1. Navigate to the **Home** page
2. Enter a title for your project
3. Upload your data file (CSV, XLS, or XLSX)
4. Preview and edit your data if needed

### Step 2: Create Visualizations
1. Go to the **Visualisation** page
2. Choose your chart type from the sidebar menu
3. Select appropriate columns for X and Y axes
4. Click "Add Chart" to save the visualization

### Step 3: View Your Report
1. Visit the **Results** page
2. See all your saved charts in one comprehensive dashboard
3. Your custom project title will be displayed at the top

## 📁 Project Structure

```
Data-visualization-/
├── 🏠️_Home.py              # Main entry point - file upload and data editing
├── pages/
│   ├── 📈_Visualisation.py  # Chart creation interface
│   ├── 😎_Results.py        # Dashboard for viewing saved charts
│   └── 📧_Contact.py        # Contact form
├── test data/               # Sample datasets for testing
│   ├── gapminder.csv        # World development indicators
│   └── ...                  # Additional sample files
├── tek_up.png              # Application logo
├── tek_up_black.png        # Alternative logo
└── README.md               # This file
```

## 🛠️ Technical Stack

- **Framework**: [Streamlit](https://streamlit.io/) - For the web interface
- **Visualization**: [Plotly](https://plotly.com/python/) - Interactive charts
- **Data Processing**: [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
- **UI Components**: [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu)
- **Image Processing**: [Pillow](https://pillow.readthedocs.io/)

## 📊 Sample Data

The application includes sample datasets in the `test data/` folder:
- **Gapminder Dataset**: Country-level data including life expectancy, population, and GDP per capita from 1952-2007
- **Product Data**: Sample business datasets for testing different chart types

## 🎯 Supported File Formats

- **CSV** (`.csv`) - Comma-separated values
- **Excel** (`.xlsx`, `.xls`) - Microsoft Excel files

## 📈 Chart Types Guide

| Chart Type | Best For | Required Data |
|------------|----------|---------------|
| **Line Chart** | Time series, trends | Categorical X-axis, Numeric Y-axis |
| **Bar Chart** | Category comparison | Categorical X-axis, Numeric Y-axis |
| **Scatter Plot** | Relationships, correlations | Numeric X-axis, Numeric Y-axis |
| **Pie Chart** | Proportions, percentages | Categorical labels, Numeric values |
| **Box Plot** | Statistical distributions | Multiple numeric columns |
| **Histogram** | Frequency distributions | Single numeric column |

## 🔧 Configuration

The application uses Streamlit's page configuration with:
- **Wide layout** for visualization pages
- **Centered layout** for forms
- **Custom icons** for each page
- **Responsive design** that works on different screen sizes

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Report Bugs**: Open an issue describing the problem
2. **Suggest Features**: Propose new chart types or functionality
3. **Submit Pull Requests**: Fix bugs or add new features
4. **Improve Documentation**: Help make this README even better

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description

## 🐛 Known Issues

- Contact form is for display purposes only (no email functionality)
- Limited error handling for malformed data files
- No data export functionality currently available

## 🚧 Future Enhancements

- [ ] Export charts as PNG/PDF
- [ ] Advanced data filtering and transformation
- [ ] More chart types (bubble charts, heatmaps)
- [ ] Real-time data connections
- [ ] User authentication and saved projects
- [ ] Advanced statistical analysis tools

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](../../issues) page for existing solutions
2. Create a new issue if your problem isn't already reported
3. Use the Contact page within the application

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Visualizations powered by [Plotly](https://plotly.com/)
- Icons and emojis for enhanced user experience

---

**Made with ❤️ for the data visualization community**