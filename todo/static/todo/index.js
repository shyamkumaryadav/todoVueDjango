var app = new Vue({
    el: '#app',
    data: {
        todos: [
            { text: "Hope 1" },
            { text: "Hope 2" },
            { text: "Hope 3" },
            { text: "Hope 4" },
        ]
    },
    methods:{
        say: (e) => {
            alert(e.target.value);
        },
        clear: (e) => {
            e.target.value = ''
        }
    }
})
