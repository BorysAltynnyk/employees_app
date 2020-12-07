(function () {
    function deleteDepartment(id) {
        return fetch('/api/departments/' + id, {
            method: 'DELETE',
        })
            .then(res => res.json())
            .then(res => console.log(res))

    }

    const table = document.querySelector('.department-table')
    table.addEventListener('click', (e) => {
        const el = e.target
        if (el.className.indexOf("delete-btn") !== -1) {
            const parent = el.closest('.department-item')
            const id = parent.getAttribute('data-id')
            deleteDepartment(id).finally(() => {
                window.location.reload()
            })
        }

    })
})()

