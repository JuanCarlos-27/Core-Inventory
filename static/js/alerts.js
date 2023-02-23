(function(){

    $("#btnDeleteProduct").forEach(btn =>{
        btn.addEventListener('click', (e)=>{
            const confirmacion = confirm("Seguro");
    
            if(!confirmacion){
                e.preventDefault()
            };
        })
    }) 
})();
