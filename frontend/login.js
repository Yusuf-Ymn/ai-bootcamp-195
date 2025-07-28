document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const loginButton = document.getElementById('login-button');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const errorMessage = document.getElementById('login-error');
    const successMessage = document.getElementById('login-success');

    // API Sözleşmesi'ne dayalı sahte (mock) API fonksiyonu
    async function fakeLoginApi(email, password) {
        console.log(`Sahte API'ya istek gönderiliyor: Email: ${email}`);

        // Gerçek bir ağ gecikmesini taklit et
        await new Promise(resolve => setTimeout(resolve, 1000));

        // Başarılı giriş senaryosu
        if (email === 'test@user.com' && password === '123456') {
            return {
                success: true,
                data: {
                    access_token: 'fake_jwt_token_xyz123abc',
                    user_name: 'Dilara'
                }
            };
        }

        // Başarısız giriş senaryosu
        return {
            success: false,
            error: 'Kullanıcı adı veya şifre hatalı'
        };
    }

    loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        errorMessage.classList.add('hidden');
        successMessage.classList.add('hidden');
        loginButton.disabled = true;
        loginButton.textContent = 'Giriş Yapılıyor...';

        const email = emailInput.value;
        const password = passwordInput.value;

        try {
            const response = await fakeLoginApi(email, password);

            if (response.success) {
                // Başarılı giriş
                successMessage.textContent = `Hoş geldin, ${response.data.user_name}! Yönlendiriliyorsun...`;
                successMessage.classList.remove('hidden');

                // Oturum bilgilerini tarayıcıda sakla (simülasyon)
                localStorage.setItem('accessToken', response.data.access_token);
                localStorage.setItem('userName', response.data.user_name);

                // 2 saniye sonra ana sayfaya yönlendir
                setTimeout(() => {
                    window.location.href = 'index.html';
                }, 2000);

            } else {
                // Başarısız giriş
                throw new Error(response.error);
            }
        } catch (error) {
            errorMessage.textContent = error.message;
            errorMessage.classList.remove('hidden');
            loginButton.disabled = false;
            loginButton.textContent = 'Giriş Yap';
        }
    });
});
