    const font = 0.45359237;

    function energiaKalkulalas(){
        var tevekenyseg;
        var sulyKg;
        var perc;
        var t = tevekenysegKcal(tevekenyseg);
        var s = energiaFogyasSzorzo(sulyKg);
        var eredmenyP = document.getElementById('kcal');
        eredmenyP.textContent =  Math.round((t*s)*perc)+' kcal';
    }

    function tevekenysegKcal(tevekenyeg){
		
    }

    function energiaFogyasSzorzo(sulyInKg){
     var sulyInFont = (sulyInKg/font);
     var szorzo = Math.round((sulyInFont/20));
     return szorzo;
    }
