var app = new Vue({
    el: '#app',
    data: {
        todos: []
    },
    methods: {
        say: (e) => {
            app.todos.push({ text: e.target.value });
            e.target.value = '';
        },
        clear: (e) => {
            e.target.value = ''
        }
    }
})
