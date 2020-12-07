(function () {
    function deleteEmployee(id) {
        return fetch('/api/employees/' + id, {
            method: 'DELETE',
        })
            .then(res => res.json())
            .then(res => console.log(res))

    }

    const table = document.querySelector('.employee-table')
    table.addEventListener('click', (e) => {
        const el = e.target
        if (el.className.indexOf("delete-btn") !== -1) {
            const parent = el.closest('.employee-item')
            const id = parent.getAttribute('data-id')
            deleteEmployee(id).finally(() => {
                window.location.reload()
            })
        }

    })
})()

