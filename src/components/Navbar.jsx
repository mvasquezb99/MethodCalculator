import React from "react";
import { Link } from "react-router-dom";

function Navbar(){
    return(
        <nav className="h-14 w-full shadow-md flex flex-row justify-start items-center">
            <Link to="/" className="flex justify-center items-center text-2xl h-full w-28 text-[#00509d]">Home</Link>
        </nav>
    )
}


export default Navbar;