import './assets/main.css'

import { createApp } from 'vue'
import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';
import App from './App.vue'
import router from './router'
import "primeicons/primeicons.css";

import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Card from 'primevue/card'
import Tag from 'primevue/tag'
import Chart from 'primevue/chart'
import ProgressBar from 'primevue/progressbar'
import Avatar from 'primevue/avatar'
import Button from 'primevue/button';
import Select from 'primevue/select';
import InputText from 'primevue/inputtext';

const app = createApp(App)
app.use(PrimeVue, {
    theme: {
        preset: Aura
    },
    ripple: true
})

app.use(router)
app.component('DataTable', DataTable)
app.component('Column', Column)
app.component('Card', Card)
app.component('Tag', Tag)
app.component('Chart', Chart)
app.component('ProgressBar', ProgressBar)
app.component('Avatar', Avatar)
app.component('Button', Button)
app.component('Select', Select)
app.component('InputText', InputText)
app.mount('#app')
