function evaluar_edad(edad){
    if (edad>0 && edad<18){
        window.alert('Es menor de edad')
    }else if(edad>=18 && edad<60){
            window.alert('Es mayor de edad')
    }else if(edad>=60 && edad<=110){
        window.alert('Es de la tercera edad')
    }else{
        window.alert('Edad no valida')
    }
}