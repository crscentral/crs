document.addEventListener('DOMContentLoaded', () => {
  // ==========================================================================
  // 1. Language Initialization & Translation Engine
  // ==========================================================================
  const langSelector = document.querySelector('.lang-selector');
  const langBtn = document.querySelector('.lang-btn');
  const langOptions = document.querySelectorAll('.lang-option');
  
  // Get saved language or default to English
  let currentLang = localStorage.getItem('crs_lang') || 'en';
  
  // Update button text with current language label
  function updateLangBtnLabel(lang) {
    if (!langBtn) return;
    const labels = {
      'en': 'English',
      'th': 'ภาษาไทย',
      'zh': '中文',
      'ar': 'العربية',
      'vi': 'Tiếng Việt',
      'km': 'ភាសាខ្មែរ'
    };
    langBtn.textContent = labels[lang] || 'English';
  }

  // Set Language and Apply Translations
  function setLanguage(lang) {
    if (!translations[lang]) return;
    
    currentLang = lang;
    localStorage.setItem('crs_lang', lang);
    updateLangBtnLabel(lang);

    // Dynamic RTL text direction support
    if (lang === 'ar') {
      document.documentElement.setAttribute('dir', 'rtl');
      document.documentElement.setAttribute('lang', 'ar');
    } else {
      document.documentElement.setAttribute('dir', 'ltr');
      document.documentElement.setAttribute('lang', lang);
    }
    
    // Smooth transition
    const i18nElements = document.querySelectorAll('[data-i18n]');
    i18nElements.forEach(el => {
      el.classList.add('translating');
    });
    
    setTimeout(() => {
      // Translate text/HTML contents
      i18nElements.forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang][key]) {
          // Check if we should insert as HTML (e.g. for spans/breaks)
          if (el.tagName === 'SPAN' || el.getAttribute('data-i18n-html') === 'true' || el.innerHTML.includes('<span') || el.innerHTML.includes('<br')) {
            el.innerHTML = translations[lang][key];
          } else {
            el.textContent = translations[lang][key];
          }
        }
        el.classList.remove('translating');
      });
      
      // Translate placeholders
      const placeholderElements = document.querySelectorAll('[data-i18n-placeholder]');
      placeholderElements.forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (translations[lang][key]) {
          el.setAttribute('placeholder', translations[lang][key]);
        }
      });

      // Dynamic page title translation for articles
      const blogArticleTitleEl = document.querySelector('article h1[data-i18n]');
      if (blogArticleTitleEl) {
        const key = blogArticleTitleEl.getAttribute('data-i18n');
        if (translations[lang][key]) {
          document.title = translations[lang][key] + " — CRS Central";
        }
      }

      // Refresh calculator text outputs with translated period indicators
      if (typeof calculateUplift === 'function') {
        calculateUplift();
      }
    }, 150);
    
    // Update active class on options
    langOptions.forEach(opt => {
      if (opt.getAttribute('data-lang') === lang) {
        opt.classList.add('active');
      } else {
        opt.classList.remove('active');
      }
    });
  }

  // Toggle Language Dropdown
  if (langBtn) {
    langBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      langSelector.classList.toggle('open');
    });
  }
  
  // Language Options Click handler
  langOptions.forEach(opt => {
    opt.addEventListener('click', () => {
      const selectedLang = opt.getAttribute('data-lang');
      setLanguage(selectedLang);
      langSelector.classList.remove('open');
    });
  });
  
  // Close language selector and nav dropdown when clicking outside
  document.addEventListener('click', () => {
    if (langSelector) {
      langSelector.classList.remove('open');
    }
    if (dropdownWrapper) {
      dropdownWrapper.classList.remove('open');
    }
  });

  // Apply default language on load
  if (typeof translations !== 'undefined') {
    setLanguage(currentLang);
  }

  // ==========================================================================
  // 2. Header Scroll Effect
  // ==========================================================================
  const header = document.querySelector('.header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // ==========================================================================
  // 3. Mobile Navigation Menu
  // ==========================================================================
  const menuToggle = document.querySelector('.menu-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const dropdownToggle = document.querySelector('.dropdown-toggle');
  const dropdownWrapper = document.querySelector('.nav-dropdown-wrapper');
  
  if (menuToggle && navMenu) {
    menuToggle.addEventListener('click', () => {
      navMenu.classList.toggle('open');
      if (navMenu.classList.contains('open')) {
        menuToggle.innerHTML = '✕';
      } else {
        menuToggle.innerHTML = '☰';
        if (dropdownWrapper) {
          dropdownWrapper.classList.remove('open');
        }
      }
    });
    
    // Close menu when clicking nav link
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        menuToggle.innerHTML = '☰';
      });
    });
    
    // Close menu when clicking nav dropdown item
    const dropdownItems = document.querySelectorAll('.nav-dropdown-item');
    dropdownItems.forEach(item => {
      item.addEventListener('click', () => {
        navMenu.classList.remove('open');
        menuToggle.innerHTML = '☰';
        if (dropdownWrapper) {
          dropdownWrapper.classList.remove('open');
        }
      });
    });
  }

  // Toggle dropdown on all devices (touch and click friendly)
  if (dropdownToggle && dropdownWrapper) {
    dropdownToggle.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropdownWrapper.classList.toggle('open');
    });
  }

  // ==========================================================================
  // 4. Highlight Active Navigation Page
  // ==========================================================================
  const currentPath = window.location.pathname;
  const pageName = currentPath.substring(currentPath.lastIndexOf('/') + 1);
  const activeLink = document.querySelector(`.nav-link[href="${pageName}"]`) || 
                     document.querySelector(`.nav-dropdown-item[href="${pageName}"]`) ||
                     (pageName === '' ? document.querySelector('.nav-link[href="index.html"]') : null);
  
  if (activeLink) {
    activeLink.classList.add('active');
    
    // If it is a dropdown item, also highlight the parent toggle button
    if (activeLink.classList.contains('nav-dropdown-item')) {
      const parentToggle = activeLink.closest('.nav-dropdown-wrapper')?.querySelector('.dropdown-toggle');
      if (parentToggle) {
        parentToggle.classList.add('active');
      }
    }
  }

  // ==========================================================================
  // 5. FAQ Accordion Trigger
  // ==========================================================================
  const faqQuestions = document.querySelectorAll('.faq-question');
  faqQuestions.forEach(q => {
    q.addEventListener('click', () => {
      const parent = q.parentElement;
      const isOpen = parent.classList.contains('open');
      
      // Close all open FAQs
      document.querySelectorAll('.faq-item').forEach(item => {
        item.classList.remove('open');
        item.querySelector('.faq-answer').style.maxHeight = null;
      });
      
      // If clicked item was not open, open it
      if (!isOpen) {
        parent.classList.add('open');
        const answer = parent.querySelector('.faq-answer');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  // ==========================================================================
  // 6. Contact & Audit Form Submissions (FormSubmit Standard Navigation)
  // ==========================================================================
  const auditForm = document.getElementById('auditForm');
  const contactForm = document.getElementById('contactForm');
  const homeAuditForm = document.getElementById('homeAuditForm');

  // Resolve dynamic thank-you redirection URL absolute path
  function resolveThanksUrl() {
    if (window.location.protocol.startsWith('http')) {
      const currentDir = window.location.pathname.substring(0, window.location.pathname.lastIndexOf('/'));
      return window.location.origin + currentDir + '/thanks.html';
    }
    return 'https://crscentral.com/thanks.html'; // Live fallback
  }

  // Inject dynamic thanks redirect to all hidden next inputs
  const nextInputs = document.querySelectorAll('.formsubmit-next');
  const thanksUrl = resolveThanksUrl();
  nextInputs.forEach(input => {
    input.value = thanksUrl;
  });

  function handleFormSubmit(event, formEl) {
    // Basic Client-Side Validation
    let isValid = true;
    const requiredInputs = formEl.querySelectorAll('[required]');
    
    requiredInputs.forEach(input => {
      if (!input.value.trim()) {
        isValid = false;
        input.style.borderColor = '#dc2626'; // Alert Red
      } else {
        input.style.borderColor = 'var(--border-color)';
      }
    });
    
    if (!isValid) {
      event.preventDefault();
      alert(currentLang === 'th' ? 'กรุณากรอกข้อมูลในช่องที่จำเป็น (*) ให้ครบถ้วน' :
            currentLang === 'zh' ? '请填写所有必填字段 (*)' :
            'Please fill in all required fields (*)');
      return;
    }
    
    // Change submit button text to sending status (do NOT disable the button so standard POST submits normally)
    const submitBtn = formEl.querySelector('button[type="submit"]');
    if (submitBtn) {
      submitBtn.textContent = currentLang === 'th' ? 'กำลังส่ง...' : currentLang === 'zh' ? '发送中...' : 'Sending...';
    }
  }

  if (auditForm) {
    auditForm.addEventListener('submit', (e) => handleFormSubmit(e, auditForm));
  }
  
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => handleFormSubmit(e, contactForm));
  }

  if (homeAuditForm) {
    homeAuditForm.addEventListener('submit', (e) => handleFormSubmit(e, homeAuditForm));
  }

  // Auto-fill https:// for Hotel Website input field
  const hotelWebsiteInput = document.getElementById('hotelWebsite');
  if (hotelWebsiteInput) {
    hotelWebsiteInput.addEventListener('focus', function() {
      if (!this.value.trim()) {
        this.value = 'https://';
        // Place cursor at the end of "https://"
        setTimeout(() => {
          this.setSelectionRange(this.value.length, this.value.length);
        }, 10);
      }
    });

    hotelWebsiteInput.addEventListener('input', function() {
      const val = this.value.trim();
      if (!val) return;

      const hasProtocol = /^https?:\/\//i.test(val);
      const isPrefix = 'https://'.startsWith(val.toLowerCase()) || 'http://'.startsWith(val.toLowerCase());

      if (!hasProtocol && !isPrefix) {
        this.value = 'https://' + val;
        // Keep the text cursor at the end of the input
        this.setSelectionRange(this.value.length, this.value.length);
      }
    });

    hotelWebsiteInput.addEventListener('blur', function() {
      const val = this.value.trim();
      if (val === 'https://' || val === 'http://') {
        this.value = '';
      } else if (val && !/^https?:\/\//i.test(val)) {
        this.value = 'https://' + val;
      }
    });
  }

  // ==========================================================================
  // 6.5. Revenue Growth Calculator Integration with Live Currency Rates
  // ==========================================================================
  // ==========================================================================
  // 6.5. Revenue Growth Calculator Integration with Live Currency Rates
  // ==========================================================================
  const calcInventory = document.getElementById('calcInventory');
  const calcInventoryRange = document.getElementById('calcInventoryRange');
  const calcOccupied = document.getElementById('calcOccupied');
  const calcOccupiedRange = document.getElementById('calcOccupiedRange');
  const calcOccupancy = document.getElementById('calcOccupancy');
  const calcOccupancyRange = document.getElementById('calcOccupancyRange');
  const calcADR = document.getElementById('calcADR');
  const calcADRRange = document.getElementById('calcADRRange');
  const calcCurrency = document.getElementById('calcCurrency');
  const calcCurrencyCode = document.getElementById('calcCurrencyCode');
  const calcExchangeRateInput = document.getElementById('calcExchangeRateInput');
  const calcExchangeRateCurrency = document.getElementById('calcExchangeRateCurrency');

  const valCurrentRev = document.getElementById('valCurrentRev');
  const valGrowth10 = document.getElementById('valGrowth10');
  const valGrowth20 = document.getElementById('valGrowth20');
  const valGrowth30 = document.getElementById('valGrowth30');
  const valExtra10 = document.getElementById('valExtra10');
  const valExtra20 = document.getElementById('valExtra20');
  const valExtra30 = document.getElementById('valExtra30');

  const btnMonthly = document.getElementById('btnMonthly');
  const btnAnnual = document.getElementById('btnAnnual');

  // Currency configuration defining symbols, slider limits and step increments
  const currencyConfigs = {
    THB: { symbol: '฿', min: 300, max: 15000, step: 100, default: 2500 },
    USD: { symbol: '$', min: 10, max: 500, step: 5, default: 80 },
    LAK: { symbol: '₭', min: 200000, max: 10000000, step: 50000, default: 1800000 },
    INR: { symbol: '₹', min: 500, max: 25000, step: 100, default: 6000 },
    GBP: { symbol: '£', min: 10, max: 400, step: 5, default: 65 },
    EUR: { symbol: '€', min: 10, max: 450, step: 5, default: 75 },
    AUD: { symbol: 'A$', min: 20, max: 700, step: 10, default: 120 },
    CNY: { symbol: '¥', min: 70, max: 3500, step: 20, default: 550 },
    JPY: { symbol: '¥', min: 1500, max: 75000, step: 500, default: 12000 },
    SGD: { symbol: 'S$', min: 15, max: 700, step: 10, default: 110 },
    HKD: { symbol: 'HK$', min: 80, max: 4000, step: 50, default: 600 }
  };

  // Live currency rates map with fallback default values relative to 1 USD
  let currentCurrency = 'THB';
  let calcPeriod = 'monthly';
  let exchangeRates = {
    THB: 36.75,
    USD: 1.0,
    LAK: 21850.0,
    INR: 83.50,
    GBP: 0.785,
    EUR: 0.912,
    AUD: 1.494,
    CNY: 7.245,
    JPY: 156.40,
    SGD: 1.345,
    HKD: 7.812
  };

  // Fetch live exchange rates from public API
  async function fetchLiveExchangeRates() {
    try {
      const response = await fetch('https://open.er-api.com/v6/latest/USD');
      if (!response.ok) throw new Error('Network response was not ok');
      const data = await response.json();
      if (data && data.result === 'success' && data.rates) {
        // Overwrite exchange rates with live values
        Object.keys(exchangeRates).forEach(code => {
          if (data.rates[code]) {
            exchangeRates[code] = data.rates[code];
          }
        });
        console.log('Live exchange rates loaded:', exchangeRates);
        updateExchangeRateIndicator();
        calculateUplift();
      }
    } catch (error) {
      console.warn('Failed to fetch live exchange rates, using fallbacks:', error);
      updateExchangeRateIndicator();
    }
  }

  function updateExchangeRateIndicator() {
    if (!calcExchangeRateInput || !calcExchangeRateCurrency) return;
    const rate = exchangeRates[currentCurrency];
    calcExchangeRateInput.value = rate.toFixed(2);
    calcExchangeRateCurrency.textContent = currentCurrency;
    
    if (currentCurrency === 'USD') {
      calcExchangeRateInput.disabled = true;
    } else {
      calcExchangeRateInput.disabled = false;
    }
  }

  function formatCurrency(val) {
    const config = currencyConfigs[currentCurrency] || { symbol: '$' };
    return config.symbol + Math.round(val).toLocaleString('en-US');
  }

  function calculateUplift() {
    if (!calcInventory || !calcOccupied || !calcOccupancy || !calcADR) return;

    const inventory = parseFloat(calcInventory.value) || 0;
    const occupied = parseFloat(calcOccupied.value) || 0;
    const occupancy = parseFloat(calcOccupancy.value) || 0;
    const adr = parseFloat(calcADR.value) || 0;

    // Days in selected period
    const days = calcPeriod === 'annual' ? 365 : 30;
    const periodText = (translations[currentLang] && translations[currentLang][calcPeriod === 'annual' ? 'calc-out-per-year' : 'calc-out-per-month']) || 
                       (calcPeriod === 'annual' ? 'per year' : 'per month');
    const extraText = (translations[currentLang] && translations[currentLang][calcPeriod === 'annual' ? 'calc-out-extra-year' : 'calc-out-extra-month']) || 
                      (calcPeriod === 'annual' ? 'extra/year' : 'extra/month');

    // Current metrics
    const currentRev = adr * occupied * days;
    const currentRevPAR = adr * (occupancy / 100);

    // Update Current Revenue Card
    if (valCurrentRev) valCurrentRev.textContent = formatCurrency(currentRev);
    
    const valCurrentOcc = document.getElementById('valCurrentOcc');
    const valCurrentADR = document.getElementById('valCurrentADR');
    const valCurrentRevPAR = document.getElementById('valCurrentRevPAR');
    
    if (valCurrentOcc) valCurrentOcc.textContent = occupancy.toFixed(1) + '%';
    if (valCurrentADR) valCurrentADR.textContent = formatCurrency(adr);
    if (valCurrentRevPAR) valCurrentRevPAR.textContent = formatCurrency(currentRevPAR);

    // Update subtext labels under Current Revenue
    const currentRevCard = valCurrentRev?.closest('.calc-output-card');
    if (currentRevCard) {
      const subEl = currentRevCard.querySelector('.calc-output-sub');
      if (subEl) subEl.textContent = periodText;
    }

    // Helper to calculate and set growth card metrics
    function setGrowthCard(percent, factor, valGrowth, valOcc, valADR, valRevPAR, valExtra) {
      const targetOcc = Math.min(100, occupancy * factor);
      const targetRev = adr * (inventory * (targetOcc / 100)) * days;
      const targetRevPAR = adr * (targetOcc / 100);
      const extraRev = targetRev - currentRev;

      if (valGrowth) valGrowth.textContent = formatCurrency(targetRev);
      if (valOcc) valOcc.textContent = targetOcc.toFixed(1) + '%';
      if (valADR) valADR.textContent = formatCurrency(adr);
      if (valRevPAR) valRevPAR.textContent = formatCurrency(targetRevPAR);
      if (valExtra) valExtra.textContent = '+' + formatCurrency(extraRev) + ' ' + extraText;
    }

    setGrowthCard(
      10, 1.10,
      document.getElementById('valGrowth10'),
      document.getElementById('valGrowthOcc10'),
      document.getElementById('valGrowthADR10'),
      document.getElementById('valGrowthRevPAR10'),
      document.getElementById('valExtra10')
    );

    setGrowthCard(
      20, 1.20,
      document.getElementById('valGrowth20'),
      document.getElementById('valGrowthOcc20'),
      document.getElementById('valGrowthADR20'),
      document.getElementById('valGrowthRevPAR20'),
      document.getElementById('valExtra20')
    );

    setGrowthCard(
      30, 1.30,
      document.getElementById('valGrowth30'),
      document.getElementById('valGrowthOcc30'),
      document.getElementById('valGrowthADR30'),
      document.getElementById('valGrowthRevPAR30'),
      document.getElementById('valExtra30')
    );
  }

  // Synchronize Inventory, Occupied Rooms, and Occupancy %
  function syncInventoryOccupancy(source) {
    if (!calcInventory || !calcOccupied || !calcOccupancy) return;
    
    let inventory = parseFloat(calcInventory.value) || 100;
    let occupied = parseFloat(calcOccupied.value) || 65;
    let occupancy = parseFloat(calcOccupancy.value) || 65;
    
    // Update occupied limits
    calcOccupied.max = inventory;
    calcOccupiedRange.max = inventory;
    
    if (source === 'inventory') {
      // Keep occupancy % constant, adjust occupied rooms
      occupied = Math.round(inventory * (occupancy / 100));
      occupied = Math.max(1, Math.min(inventory, occupied));
      calcOccupied.value = occupied;
      calcOccupiedRange.value = occupied;
    } else if (source === 'occupied') {
      // Adjust occupancy % based on new occupied rooms
      if (occupied > inventory) {
        occupied = inventory;
        calcOccupied.value = occupied;
        calcOccupiedRange.value = occupied;
      }
      occupancy = parseFloat(((occupied / inventory) * 100).toFixed(1));
      calcOccupancy.value = occupancy;
      calcOccupancyRange.value = occupancy;
    } else if (source === 'occupancy') {
      // Adjust occupied rooms based on new occupancy %
      occupied = Math.round(inventory * (occupancy / 100));
      occupied = Math.max(1, Math.min(inventory, occupied));
      calcOccupied.value = occupied;
      calcOccupiedRange.value = occupied;
    }
  }

  // Setup range slider and number input synchronization
  function bindSliderSync(numInput, rangeInput, onSyncCallback) {
    if (!numInput || !rangeInput) return;

    numInput.addEventListener('input', () => {
      let val = parseFloat(numInput.value);
      const min = parseFloat(numInput.min) || 0;
      const max = parseFloat(numInput.max) || 1000000;
      
      if (isNaN(val)) val = min;
      if (val < min) val = min;
      if (val > max) val = max;
      
      rangeInput.value = val;
      if (onSyncCallback) onSyncCallback();
      calculateUplift();
    });

    rangeInput.addEventListener('input', () => {
      numInput.value = rangeInput.value;
      if (onSyncCallback) onSyncCallback();
      calculateUplift();
    });
  }

  // Handle custom exchange rate manual input
  if (calcExchangeRateInput) {
    calcExchangeRateInput.addEventListener('input', () => {
      const val = parseFloat(calcExchangeRateInput.value);
      if (!isNaN(val) && val > 0) {
        exchangeRates[currentCurrency] = val;
        calculateUplift();
      }
    });
  }

  // Handle currency changes
  if (calcCurrency) {
    calcCurrency.addEventListener('change', () => {
      const oldCurrency = currentCurrency;
      const newCurrency = calcCurrency.value;
      currentCurrency = newCurrency;
      
      // Update label suffix
      if (calcCurrencyCode) {
        calcCurrencyCode.textContent = newCurrency;
      }
      
      // Convert current ADR to new currency
      const config = currencyConfigs[newCurrency];
      const oldRate = exchangeRates[oldCurrency];
      const newRate = exchangeRates[newCurrency];
      
      let oldADR = parseFloat(calcADR.value) || 0;
      let newADR = oldADR * (newRate / oldRate);
      
      // Round converted ADR value to sensible values (no decimals)
      newADR = Math.round(newADR);
      
      // Clamp to currency range boundaries
      newADR = Math.max(config.min, Math.min(config.max, newADR));
      
      // Update ADR slider and input attributes
      calcADR.min = config.min;
      calcADR.max = config.max;
      calcADRRange.min = config.min;
      calcADRRange.max = config.max;
      calcADRRange.step = config.step;
      
      calcADR.value = newADR;
      calcADRRange.value = newADR;
      
      // Update exchange rate indicators
      updateExchangeRateIndicator();
      calculateUplift();
    });
  }

  // Handle period toggle clicks
  if (btnMonthly && btnAnnual) {
    btnMonthly.addEventListener('click', () => {
      btnMonthly.classList.add('active');
      btnAnnual.classList.remove('active');
      calcPeriod = 'monthly';
      calculateUplift();
    });

    btnAnnual.addEventListener('click', () => {
      btnAnnual.classList.add('active');
      btnMonthly.classList.remove('active');
      calcPeriod = 'annual';
      calculateUplift();
    });
  }

  if (calcInventory && calcInventoryRange) {
    // Sync initial state limits
    syncInventoryOccupancy('inventory');

    // Bind slider events
    bindSliderSync(calcInventory, calcInventoryRange, () => syncInventoryOccupancy('inventory'));
    bindSliderSync(calcOccupied, calcOccupiedRange, () => syncInventoryOccupancy('occupied'));
    bindSliderSync(calcOccupancy, calcOccupancyRange, () => syncInventoryOccupancy('occupancy'));
    bindSliderSync(calcADR, calcADRRange, null);
    
    // Initial rates load & setup
    fetchLiveExchangeRates();
  }

  // ==========================================================================
  // 7. Floating WhatsApp Button
  // ==========================================================================
  const whatsappBtn = document.createElement('a');
  whatsappBtn.href = 'https://wa.me/66990143142';
  whatsappBtn.target = '_blank';
  whatsappBtn.rel = 'noopener noreferrer';
  whatsappBtn.className = 'whatsapp-float';
  whatsappBtn.setAttribute('aria-label', 'Chat on WhatsApp');
  whatsappBtn.innerHTML = `
    <svg viewBox="0 0 24 24" class="whatsapp-icon">
      <path fill="#ffffff" d="M12.012 2c-5.506 0-9.989 4.478-9.99 9.984a9.964 9.964 0 0 0 1.333 4.993L2 22l5.233-1.371a9.936 9.936 0 0 0 4.777 1.216h.005c5.505 0 9.989-4.478 9.99-9.984 0-2.669-1.037-5.176-2.922-7.062C17.198 2.914 14.69 2.003 12.012 2zm5.726 14.126c-.253.712-1.256 1.309-1.72 1.414-.465.105-.91.147-2.812-.605-2.433-.962-3.99-3.43-4.11-3.593-.122-.162-1.002-1.332-1.002-2.54 0-1.21.632-1.804.856-2.046.225-.242.49-.302.653-.302.164 0 .328.001.47.009.15.008.354-.057.555.424.201.483.693 1.688.754 1.808.06.12.101.26.02.422-.08.162-.122.262-.243.402-.12.14-.256.312-.366.42-.12.116-.246.242-.106.483.14.241.623 1.026 1.335 1.66.918.816 1.69 1.07 1.936 1.19.246.12.39.102.533-.06.143-.162.613-.714.777-.957.164-.241.328-.201.554-.117.227.085 1.432.677 1.678.799.246.122.41.18.47.288.061.108.061.624-.192 1.336z"/>
    </svg>
    <span class="whatsapp-tooltip">Chat on WhatsApp</span>
  `;
  document.body.appendChild(whatsappBtn);
});
