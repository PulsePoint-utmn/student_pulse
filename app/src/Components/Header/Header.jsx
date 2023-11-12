import React from "react";

function Header() {
    return ( 
        <div className="flex justify-between px-8">
            <span>StudentPuse</span>
            <div className="login">
                <a href="/register" >Register</a> | <a href="/login" >Login</a>
            </div>
        </div>
     );
}

export default Header;