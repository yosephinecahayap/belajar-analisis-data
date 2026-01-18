import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="E-Commerce Dashboard",
    layout="wide"
)

st.title("E-Commerce Transaction Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv(
        "dashboard/data.csv",
        parse_dates=[
            'order_purchase_timestamp',
            'order_approved_at',
            'order_delivered_customer_date',
            'order_estimated_delivery_date'
        ]
    )

data = load_data()

st.sidebar.header("Filter Data")

data['year'] = data['order_purchase_timestamp'].dt.year

# Filter Tahun
selected_year = st.sidebar.multiselect(
    "Pilih Tahun",
    options=sorted(data['year'].unique()),
    default=sorted(data['year'].unique())
)

selected_category = st.sidebar.multiselect(
    "Pilih Kategori Produk",
    options=sorted(data['product_category_name_english'].dropna().unique()),
    default=None
)

selected_payment = st.sidebar.multiselect(
    "Pilih Tipe Pembayaran",
    options=sorted(data['payment_type'].dropna().unique()),
    default=None
)

filtered_data = data[data['year'].isin(selected_year)]

if selected_category:
    filtered_data = filtered_data[
        filtered_data['product_category_name_english'].isin(selected_category)
    ]

if selected_payment:
    filtered_data = filtered_data[
        filtered_data['payment_type'].isin(selected_payment)
    ]

snapshot_date = filtered_data['order_purchase_timestamp'].max() + pd.Timedelta(days=1)

rfm = filtered_data.groupby('customer_unique_id').agg({
    'order_purchase_timestamp': lambda x: (snapshot_date - x.max()).days,
    'order_id': 'nunique',
    'payment_value': 'sum'
}).reset_index()

rfm.columns = ['customer_unique_id', 'recency', 'frequency', 'monetary']

st.subheader("📌 Ringkasan Performa E-Commerce")

total_revenue = filtered_data['payment_value'].sum()
total_orders = filtered_data['order_id'].nunique()
total_customers = filtered_data['customer_unique_id'].nunique()
avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
avg_recency = rfm['recency'].mean() if not rfm.empty else 0

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Revenue", f"{total_revenue:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)
col4.metric("Avg Order Value", f"{avg_order_value:,.0f}")
col5.metric("Avg Recency (Hari)", f"{avg_recency:.1f}")

st.caption(
    f"Filter aktif → Tahun: {selected_year}, "
    f"Kategori: {selected_category if selected_category else 'Semua'}, "
    f"Pembayaran: {selected_payment if selected_payment else 'Semua'}"
)

st.subheader("Top 10 Kategori Produk dengan Revenue Tertinggi")

revenue_category = (
    filtered_data.groupby('product_category_name_english')['payment_value']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(
    x=revenue_category.values,
    y=revenue_category.index,
    ax=ax1
)
ax1.set_xlabel("Total Revenue")
ax1.set_ylabel("Kategori Produk")

st.pyplot(fig1)

st.subheader("Analisis Perilaku Pelanggan (RFM)")

fig2, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.histplot(rfm['recency'], bins=30, ax=axes[0])
axes[0].set_title("Distribusi Recency")
axes[0].set_xlabel("Hari sejak pembelian terakhir")

sns.histplot(rfm['frequency'], bins=30, ax=axes[1])
axes[1].set_title("Distribusi Frequency")
axes[1].set_xlabel("Jumlah Transaksi")

sns.histplot(rfm['monetary'], bins=30, ax=axes[2])
axes[2].set_title("Distribusi Monetary")
axes[2].set_xlabel("Total Pengeluaran")

st.pyplot(fig2)

st.caption(
    "Dashboard dibuat menggunakan Streamlit | Analisis Data E-Commerce | Yosephine Cahaya Permatahari"
)
