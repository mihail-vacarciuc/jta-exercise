<template>
    <div class="home-view">
        <div>
            <h1>Dashboard</h1>
            <p>Overview of Users and products</p>
        </div>

        <!-- KPI -->
        <div class="kpi-grid">
            <Card>
                <template #content>
                    <div>
                        <i class="pi pi-users" />
                        <div>
                            <p>Total Users</p>
                            <p>{{totalUsers}}</p>
                        </div>
                    </div>
                </template>
            </Card>

            <Card>
                <template #content>
                    <div>
                        <i class="pi pi-box" />
                        <div>
                            <p>Total Products</p>
                            <p>{{totalProducts}}</p>
                        </div>
                    </div>
                </template>
            </Card>

            <Card>
                <template #content>
                    <div>
                        <i class="pi pi-tag" />
                        <div>
                            <p>Avg Product Price</p>
                            <p>${{avgPrice}}</p>
                        </div>
                    </div>
                </template>
            </Card>

            <Card>
                <template #content>
                    <div>
                        <i class="pi pi-warehouse" />
                        <div>
                            <p>Total Stock</p>
                            <p>{{avgStock}}</p>
                        </div>
                    </div>
                </template>
            </Card>
        </div>

        <!--Mini charts-->
        <div class="charts-grid">
            <Card>
                <template #title>Users by State (Top 8)</template>
                <template #content>
                    <Chart v-if="stateChartData" type="bar" :data="stateChartData"  />
                </template>
            </Card>
            <Card>
                <template #title>Produts by category</template>
                <template #content>
                    <Chart v-if="categoryChartData" type="bar" :data="categoryChartData" />
                </template>
            </Card>
        </div>
    </div>
</template>

<script setup>
import { onMounted, computed, ref } from 'vue'
import { getUsersAnalytics, getProductsAnalytics } from '../api/client'

const users_analytics = ref(null)
const products_analytics = ref(null)

onMounted(async() => {
    try{
        users_analytics.value = await getUsersAnalytics()
        products_analytics.value = await getProductsAnalytics()

        console.log(users_analytics.value)
        console.log(products_analytics.value)
    }catch (error){
        console.error('Failed to load users: ', error)
    }
})


const totalUsers = computed(() => users_analytics.value?.TotalUsers ?? 0)
const totalProducts = computed(() => products_analytics.value?.TotalProducts ?? 0)
const avgPrice = computed(() => products_analytics.value?.AvgPrice ?? 0)
const avgStock = computed(() => products_analytics.value?.TotalStock ?? 0)

//Charts
const stateChartData = computed(() => {
   if (!users_analytics.value) return null
   return{
        labels: users_analytics.value.byState.labels.slice(0, 8),
        datasets:[{
            label: 'Users',
            data: users_analytics.value.byState.values.slice(0, 8)
        }]
   }
})

const categoryChartData = computed(() => {
   if (!products_analytics.value) return null
   return{
        labels: products_analytics.value.byCategory.labels,
        datasets:[{
            label: 'Categories',
            data: products_analytics.value.byCategory.values
        }]
   }
})
</script>

<style scoped>
.home-view { 
    display: flex; 
    flex-direction: 
    column; gap: 1.5rem; 
}
.kpi-grid { 
    display: grid;
    grid-template-columns: repeat(4, 1fr); 
    gap: 1rem; 
}
.charts-grid { 
    display: grid; 
    grid-template-columns: 1fr 1fr; 
    gap: 1rem; 
}
</style>