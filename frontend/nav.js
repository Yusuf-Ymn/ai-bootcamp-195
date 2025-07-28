document.addEventListener("DOMContentLoaded", function() {
    // Bu, her HTML dosyasındaki yer tutucu elementtir
    const navbarPlaceholder = document.getElementById('navbar-placeholder');

    if (navbarPlaceholder) {
        // _nav.html dosyasının içeriğini çek
        fetch('_nav.html')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Navigasyon menüsü yüklenemedi.');
                }
                return response.text();
            })
            .then(html => {
                // Çekilen HTML'i yer tutucunun içine yerleştir
                navbarPlaceholder.innerHTML = html;

                // Navigasyon yüklendikten sonra, aktif linki ayarla
                const currentPage = window.location.pathname.split('/').pop() || 'index.html';
                const navLinks = navbarPlaceholder.querySelectorAll('.nav-link');

                navLinks.forEach(linkOrButton => {
                    // Doğrudan bir link ise (<a> etiketi)
                    if (linkOrButton.tagName === 'A') {
                        const linkHref = linkOrButton.getAttribute('href');
                        if (linkHref === currentPage) {
                            linkOrButton.classList.add('active');
                        }
                    }
                    // Açılır menünün ana butonu ise
                    else if (linkOrButton.parentElement.classList.contains('group')) {
                        const dropdownLinks = linkOrButton.parentElement.querySelectorAll('.dropdown-link');
                        let isParentActive = false;
                        dropdownLinks.forEach(dropdownLink => {
                            if (dropdownLink.getAttribute('href') === currentPage) {
                                isParentActive = true;
                            }
                        });
                        if (isParentActive) {
                            linkOrButton.classList.add('active');
                        }
                    }
                });
            })
            .catch(error => {
                console.error('Navigasyon menüsü yüklenirken hata:', error);
                navbarPlaceholder.innerHTML = '<p class="text-red-500 text-center">Navigasyon menüsü yüklenemedi.</p>';
            });
    }
});
