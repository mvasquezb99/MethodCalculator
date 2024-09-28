import React from "react";
import { Link } from "react-router-dom";

function Navbar(){
    return(
        <nav className="h-14 w-full shadow-md shadow-white flex flex-row justify-start items-center bg-[#00509d]">
            <Link to="/" className="flex justify-center items-center text-2xl h-full w-28 text-[#FFFF]">Analisis</Link>
        </nav>
    )
}


export default Navbar;