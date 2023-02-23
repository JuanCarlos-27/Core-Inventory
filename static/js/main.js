window.addEventListener('load', event => {
    let dataTable;
    const dataTableOptions = {
        dom: 'Bfrtip',
        buttons: [
            {
                extend: "pdfHtml5",
                text: "PDF <i class='fas fa-file-pdf'></i>",
                titleAttr: "Exportar a PDF",
                className: "shadow btn btn-danger",
            },
            {
                extend: 'excelHtml5',
                text: 'EXCEL <i class="fas fa-file-excel"></i>',
                titleAttr: "Exportar a Excel",
                className: "shadow btn btn-success"
            },

            //  {
            //     extend: "print",
            //     text: "Imprimir <i class='fas fa-print'></i>",
            //     titleAttr:"Imprimir",
            //     className: "shadow btn btn-info"
            //  },
        ],
        language: {
            lengthMenu: "Mostrar _MENU_ registros por página",
            zeroRecords: "Ningún registro encontrado",
            info: "Mostrando de _START_ a _END_ de un total de _TOTAL_ registros",
            infoEmpty: "Ningún registro encontrado",
            infoFiltered: "(Filtrados desde _MAX_ registros totales)",
            search: "Buscar:",
            loadingRecords: "Cargando...",
            paginate: {
                first: "Primero",
                last: "Último",
                next: "Siguiente",
                previous: "Anterior"
            }
        }
    }
    const initDataTable = () => {
        $("#dataTable_product").DataTable(dataTableOptions);
    };
    initDataTable();


    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

