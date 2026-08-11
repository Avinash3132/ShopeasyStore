// ============================================
// SHOPEASY - Main JavaScript
// ============================================

document.addEventListener('DOMContentLoaded', function () {

  // ── Quantity Controls (Product Detail Page) ──
  const qtyInput = document.getElementById('quantity');
  const qtyMinus = document.getElementById('qty-minus');
  const qtyPlus  = document.getElementById('qty-plus');

  if (qtyInput && qtyMinus && qtyPlus) {
    const max = parseInt(qtyInput.getAttribute('max')) || 99;

    qtyMinus.addEventListener('click', function() {
      let v = parseInt(qtyInput.value) || 1;
      if (v > 1) {
        qtyInput.value = v - 1;
      }
    });

    qtyPlus.addEventListener('click', function() {
      let v = parseInt(qtyInput.value) || 1;
      if (v < max) {
        qtyInput.value = v + 1;
      }
    });

    qtyInput.addEventListener('change', function() {
      let v = parseInt(qtyInput.value) || 1;
      if (v < 1) qtyInput.value = 1;
      if (v > max) qtyInput.value = max;
    });
  }

  // ── Auto-dismiss alerts ──
  setTimeout(function() {
    document.querySelectorAll('.alert-dismissible').forEach(function(el) {
      el.style.transition = 'opacity 0.5s';
      el.style.opacity = '0';
      setTimeout(function() { el.remove(); }, 500);
    });
  }, 3500);

});