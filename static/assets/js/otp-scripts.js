document.addEventListener('DOMContentLoaded', function() {
    // Auto focus and move between OTP inputs
    const otpInputs = document.querySelectorAll('.otp-inputs input');
    
    otpInputs.forEach((input, index) => {
        input.addEventListener('input', function(e) {
            if (this.value.length === 1) {
                if (index < otpInputs.length - 1) {
                    otpInputs[index + 1].focus();
                }
            }
        });
        
        input.addEventListener('keydown', function(e) {
            if (e.key === 'Backspace' && this.value.length === 0) {
                if (index > 0) {
                    otpInputs[index - 1].focus();
                }
            }
        });
    });
    
    // Timer countdown
    let timeLeft = 180; // 3 minutes in seconds
    const timerElement = document.getElementById('timer');
    const resendLink = document.getElementById('resend-otp');
    
    function updateTimer() {
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        
        timerElement.textContent = `${minutes.toString().padStart(2, '۰')}:${seconds.toString().padStart(2, '۰')}`;
        
        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            timerElement.style.color = '#2ecc71';
            timerElement.textContent = 'کد منقضی شده است';
            resendLink.classList.remove('disabled');
        } else {
            timeLeft--;
        }
    }
    
    let timerInterval = setInterval(updateTimer, 1000);
    updateTimer();
    
    // Resend OTP functionality
    resendLink.addEventListener('click', function(e) {
        e.preventDefault();
        
        if (!this.classList.contains('disabled')) {
            // Reset timer
            timeLeft = 120;
            timerElement.style.color = '#e74c3c';
            this.classList.add('disabled');
            timerInterval = setInterval(updateTimer, 1000);
            
            // Show message (simulated)
            const originalText = this.textContent;
            this.textContent = 'در حال ارسال...';
            
            setTimeout(() => {
                this.textContent = originalText;
                // In a real app, you would send the OTP here
            }, 1500);
        }
    });
    
    // Ripple effect for submit button (reusing from register.js)
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
    
    // Animation for OTP inputs
    otpInputs.forEach((input, index) => {
        setTimeout(() => {
            input.style.opacity = '1';
            input.style.transform = 'scale(1)';
        }, index * 100);
    });
});