window.addEventListener('DOMContentLoaded', event => {
    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }
    
    datatablesSimple.DataTable({
        dom:"Bfrtilp",
        buttons: [
            'excel', 'pdf'
        ]
    })
});
