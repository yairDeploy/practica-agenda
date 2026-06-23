function duplicarForm() {
    const container = document.getElementById('formset-container');
    const forms = container.querySelectorAll('.telefono-form');
    const totalForms = forms.length;
    const newIndex = totalForms;
    
    // Clonar el último formulario
    const lastForm = forms[forms.length - 1];
    const newForm = lastForm.cloneNode(true);
    
    // Limpiar formulario
    newForm.id = `form-${newIndex}`;
    
    newForm.querySelectorAll('*').forEach(element => {
        if (element.name) {
            element.name = element.name.replace(/-\d+-/, `-${newIndex}-`);
        }
        if (element.id) {
            element.id = element.id.replace(/-\d+-/, `-${newIndex}-`);
        }
        if (element.htmlFor) {
            element.htmlFor = element.htmlFor.replace(/-\d+-/, `-${newIndex}-`);
        }
        
        // Limpiar valores
        if (element.type === 'text' || element.type === 'number' || element.tagName === 'SELECT') {
            if (element.tagName === 'SELECT') {
                element.selectedIndex = 0;
            } else {
                element.value = '';
            }
        }
        if (element.type === 'checkbox') {
            element.checked = false;
        }
        if (element.type === 'hidden' && element.name && element.name.includes('-id')) {
            // ELIMINAR completamente el campo ID oculto
            element.remove();
        }
    });
    
    // Actualizar el botón
    const button = newForm.querySelector('button');
    if (button) {
        button.textContent = 'Eliminar';
        button.className = 'btn btn-sm btn-warning';
        button.setAttribute('onclick', `eliminar_As(${newIndex})`);
        // Remover atributo data o eventos anteriores
        button.removeAttribute('data-id');
    }
    
    // Agregar al contenedor
    container.appendChild(newForm);
    
    // Actualizar TOTAL_FORMS
    const totalFormsInput = document.getElementById('id_telefono_set-TOTAL_FORMS');
    if (totalFormsInput) {
        totalFormsInput.value = newIndex + 1;
    }
}
function eliminar_As(id) {
    console.log("Eliminar teléfono con ID:", id);
    const checkbox = document.getElementById(`id_telefono_set-${id}-DELETE`);
    if (checkbox) {
        
        checkbox.checked = true;
        document.getElementById(`form-${id}`).classList.add('d-none');
    }
    const totalFormsInput = document.getElementById('id_telefono_set-TOTAL_FORMS');
    if (totalFormsInput) {
        totalFormsInput.value = parseInt(totalFormsInput.value) - 1;
    }
}
function cancelar_As(id) {
    console.log("Cancelar teléfono con ID:", id);
    document.getElementById(`form-${id}`).remove();
    const totalFormsInput = document.getElementById('id_telefono_set-TOTAL_FORMS');
    if (totalFormsInput) {
        totalFormsInput.value = parseInt(totalFormsInput.value) - 1;
    }
}