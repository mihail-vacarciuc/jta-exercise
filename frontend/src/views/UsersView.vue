<template>
    <div class="users-view">
        <h1>Users</h1>
        <div class="charts-grid">
            <Card>
                <template #title>Distribution by State</template>
                <template #content>
                    <Chart v-if="stateChartData" type="bar" :data="stateChartData" />
                </template>
            </Card>
            <Card>
                <template #title>Distribution by University</template>
                <template #content>
                    <Chart v-if="uniChartData" type="pie" :data="uniChartData" />
                </template>
            </Card>
        </div>
        
        <Card>
            <template #title>
                <div>
                    <span>User Records</span>
                    <Button label="Reload" icon="pi pi-refresh" @click="loadUsers"/>
                </div>
            </template>

            <template #content>
                <DataTable
                    :value="users"
                    :loading="loading"
                    dataKey="id"
                    paginator
                    :rows="10"
                    stripedRows
                    sortMode="multiple"
                    removableSort
                    filterDisplay="row"
                    v-model:filters="filters"
                    tableStyle="min-width: 60rem">

                    <template #header>
                        <div>
                            <i class="pi pi-search" />
                            <InputText v-model="filters['global'].value" placeholder="Search..." />
                        </div>
                    </template>

                    
                    <Column field="name" header="Name" sortable/>
                    <Column field="age" header="Age" sortable/>
                    <Column field="gender" header="Gender" sortable/>
                    <Column field="state" header="State" sortable :showFilterMenu="false">
                        <template #filter="{filterModel, filterCallback}">
                            <Select
                                v-model="filterModel.value"
                                :options="stateOptions"
                                showClear
                                @change="filterCallback()"/>
                        </template>
                    </Column>
                    <Column field="university" header="University" sortable/>
                    <Column field="role" header="Role" sortable>
                        <template #filter="{filterModel, filterCallback}">
                            <Select
                                v-model="filterModel.value"
                                :options="roleOptions"
                                showClear
                                @change="filterCallback()"/>
                        </template>
                    </Column>

                </DataTable>
            </template>
        </Card>
    </div>
</template>

<script setup>
import { onMounted, computed, ref } from 'vue'
import { getUsers, getUsersAnalytics } from '../api/client'
import {FilterMatchMode} from '@primevue/core/api'

const analytics = ref(null)
const users = ref([])
const loading = ref(false)
const filters = ref({
    global: {value: null, matchMode: FilterMatchMode.CONTAINS},
    role: {value: null, matchMode: FilterMatchMode.EQUALS},
    state: {value: null, matchMode: FilterMatchMode.EQUALS}
})

async function loadUsers() {
    loading.value = true

    try {
        const data = await getUsers()
        users.value = data
        console.log(users.value[1])
    } catch (error){
        console.error('Failed to load users: ', error)
    } finally {
        loading.value = false
    }
}

onMounted(async() => {
    loadUsers()

    try{
        analytics.value = await getUsersAnalytics()
    }catch (error){
        console.error('Failed to load users: ', error)
    }
})

//Charts
const stateChartData = computed(() => {
   if (!analytics.value) return null
   return{
        labels: analytics.value.byState.labels,
        datasets:[{
            label: 'Users',
            data: analytics.value.byState.values
        }]
   }
})

const uniChartData = computed(() => {
   if (!analytics.value) return null
   return{
        labels: analytics.value.byUniversity.labels,
        datasets:[{
            label: 'Users',
            data: analytics.value.byUniversity.values
        }]
   }
})

//Filters
const roleOptions = computed(() => [...new Set(users.value.map(u => u.role).filter(Boolean))])
const stateOptions = computed(() => [...new Set(users.value.map(u => u.state).filter(Boolean))].sort())

</script>

<style scoped>
.charts-grid { 
    display: grid; 
    grid-template-columns: 1fr 1fr; 
    gap: 1rem; 
}
</style>