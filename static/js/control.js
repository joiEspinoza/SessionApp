
////////////////////////// register loading ///////////////////////////

const btnLoading = document.getElementById( "loading" );
const btnRegister = document.getElementById( "registerLogin" );

btnRegister.addEventListener( "click", () => {

    btnRegister.setAttribute( "hidden", true )
    btnLoading.removeAttribute( "hidden" )

} )

//////////////////////////////////////////////////////////////////