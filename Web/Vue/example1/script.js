Vue.component('card', {
    props:{
        image: String,
        imageDescription: String,
        headerText: String,
        bodyText: String
    },
    template:`
    <div class="card">
        <img v-bind:src="image" v-bind:alt="imageDescription">
        <div>
            <h3>{{ headerText }}</h3>
            <p>{{ bodyText }}</p>
        </div>
    </div>
    `
})

var app = new Vue({
    el: "#app",
    data:{
        ticker: ""
    },
    methods:{
        getLink: function(){
            return "https://finance.yahoo.com/chart/" + this.ticker;
        }
    }
});
