import React from "react";

function Header() {
    return ( 
        <div className="backdrop-opacity-100 top-0 text-indigo-50">
            <header>
                <ul className="list-none flex justify-center gap-4">
                <li className="p-2">Home</li>
                <li className="p-2">Blog</li>
                <li className="p-2">About</li>
                <li className="p-2">Contact</li>
                </ul>
            </header>
    </div>
     );
}

export default Header;