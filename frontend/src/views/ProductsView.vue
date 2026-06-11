<template>
    <div class="products-view">
        <h1>Product Analytics</h1>
        
        <div class="charts-grid">
            <Card>
                <template #title>Top Brands by Avg Rating</template>
                <template #content>
                    <Chart v-if="brandsChartData" type="doughnut" :data="brandsChartData" />
                </template>
            </Card>

            <Card>
                <template #title>Available Products by Category</template>
                <template #content>
                    <Chart v-if="categoryChartData" type="doughnut" :data="categoryChartData" />
                </template>
            </Card>

            <Card>
                <template #title>Price Range by Category</template>
                <template #content>
                    <Chart v-if="priceRangeChartData" type="bar" :data="priceRangeChartData"/>
                </template>
            </Card>

            <Card>
                <template #title>Stock by Products</template>
                <template #content>
                    <DataTable 
                        :value="products"
                        :loading="loading"
                        paginator
                        :rows="10"
                        sortMode="multiple"
                        stripedRows
                        dataKey="id">

                        <Column field="product" header="Product" sortable />
                        <Column field="brand" header="Brand" sortable />
                        <Column field="category" header="Category" sortable />
                        <Column field="price" header="Price" sortable>
                            <template #body="{data}">${{data.price}}</template>
                        </Column>
                        <Column field="stock" header="Stock" sortable />
                        <Column field="rating" header="Rating" sortable/>
                    </DataTable>
                </template>
            </Card>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { getProducts, getProductsAnalytics } from '../api/client'

const analytics = ref(null)
const products = ref([])
const loading = ref(false)

async function loadProducts() {
    loading.value = true

    try {
        const data = await getProducts()
        
        products.value = data
    } catch (error){
        console.error('Failed to load users: ', error)
    } finally {
        loading.value = false
    }
}

onMounted( async() => {
    loadProducts()

    try{
        analytics.value = await getProductsAnalytics()
    }catch (error){
        console.error('Failed to load users: ', error)
    }
})

//Charts
const brandsChartData = computed(() => {
   if (!analytics.value) return null
   return{
        labels: analytics.value.byBrands.labels,
        datasets:[{
            label: 'Brands',
            data: analytics.value.byBrands.values
        }]
   }
})

const categoryChartData = computed(() => {
   if (!analytics.value) return null
   return{
        labels: analytics.value.byCategory.labels,
        datasets:[{
            label: 'Categories',
            data: analytics.value.byCategory.values
        }]
   }
})

const priceRangeChartData = computed(() => {
   if (!analytics.value) return null
   return{
        labels: analytics.value.byPriceRange.labels,
        datasets:[{
            label: 'Price Range',
            data: analytics.value.byPriceRange.values
        }]
   }
})
</script>

<style scoped>
.charts-grid { 
    display: grid; 
    grid-template-columns: 1fr 1fr; 
    gap: 1rem; 
}
</style>