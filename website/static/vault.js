function hidePass() {
    var password = document.getElementById('vaultPass');
     if (password.style.display === 'none') {
         password.style.display = 'block';
     } else {
         password.style.display = 'none';
     }
 }