$(document).ready(function(){
    
    (function($) {
        "use strict";

    
    jQuery.validator.addMethod('answercheck', function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value)
    }, "type the correct answer -_-");

    // validate contactForm form
    $(function() {
        $('#contactForm').validate({
            ignore: ".ignore",
            rules: {
                nome: {
                    required: true,
                    minlength: 2
                },
                replyto: {
                    required: true,
                    minlength: 2
                },
                assunto: {
                    required: true,
                    minlength: 4
                },
                mensagem: {
                    required: true,
                    minlength: 2
                },
                hiddenRecaptcha: {
                    required: function () {
                        console.log("hiddenRecaptchaFunction")
                        if (grecaptcha.getResponse() == '') {
                            console.log("hiddenRecaptcha return true")
                            return true;
                        } else {
                            console.log("hiddenRecaptcha return false")
                            return false;
                        }
                    }
                }
                
            },
            messages: {
                nome: {
                    required: "Digite seu nome",
                    
                },
                replyto: {
                    required: "Digite seu e-mail",
                    
                },
                assunto: {
                    required: "Preencha o campo assunto",
                    
                },
                
                menssagem: {
                    required: "Digite sua mensagem",
                    
                },
                hiddenRecaptcha: {
                    required: "Confirme o Captcha"
                },
            },
            submitHandler: function(form) {
                $(form).ajaxSubmit({
                    type:"POST",
                    data: $(form).serialize(),
                    url:"contact_process.php",
                    success: function() {
                        $('#contactForm :input').attr('disabled', 'disabled');
                        $('#contactForm').fadeTo( "slow", 0.15, function() {
                            $(this).find(':input').attr('disabled', 'disabled');
                            $(this).find('label').css('cursor','default');
                            $('#success').fadeIn()
                        })
                    },
                    error: function() {
                        $('#contactForm').fadeTo( "slow", 0.15, function() {
                            $('#error').fadeIn()
                        })
                    }
                })
            }
        })
    })
        
 })(jQuery)
})