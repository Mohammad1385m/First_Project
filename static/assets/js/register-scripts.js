document.addEventListener('DOMContentLoaded', function() {
    // Toggle password visibility
    const togglePasswordButtons = document.querySelectorAll('.toggle-password');
    
    togglePasswordButtons.forEach(button => {
        button.addEventListener('click', function() {
            const input = this.parentElement.querySelector('input');
            const icon = this.querySelector('i');
            
            if (input.type === 'password') {
                input.type = 'text';
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else {
                input.type = 'password';
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        });
    });
    
    // Floating label effect for browsers that don't support :placeholder-shown
    const inputs = document.querySelectorAll('.form-group.floating input');
    
    inputs.forEach(input => {
        // Check if input has value on page load
        if (input.value) {
            const label = input.nextElementSibling;
            label.style.top = '-10px';
            label.style.right = '30px';
            label.style.fontSize = '12px';
            label.style.color = '#4a90e2';
            label.style.backgroundColor = '#fff';
        }
        
        input.addEventListener('focus', function() {
            const label = this.nextElementSibling;
            label.style.top = '-10px';
            label.style.right = '30px';
            label.style.fontSize = '12px';
            label.style.color = '#4a90e2';
            label.style.backgroundColor = '#fff';
        });
        
        input.addEventListener('blur', function() {
            if (!this.value) {
                const label = this.nextElementSibling;
                label.style.top = '15px';
                label.style.right = '45px';
                label.style.fontSize = '14px';
                label.style.color = '#999';
                label.style.backgroundColor = '#f9fafc';
            }
        });
    });
    
    // Add ripple effect to submit button
    const submitBtn = document.querySelector('.submit-btn');
    
    submitBtn.addEventListener('click', function(e) {
        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const ripple = document.createElement('span');
        ripple.className = 'ripple';
        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;
        
        this.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 1000);
    });
    
    // Add animation to form inputs on page load
    const formGroups = document.querySelectorAll('.form-group');
    
    formGroups.forEach((group, index) => {
        setTimeout(() => {
            group.style.opacity = '1';
            group.style.transform = 'translateY(0)';
        }, index * 100);
    });
});