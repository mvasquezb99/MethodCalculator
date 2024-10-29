import React from "react";
import { Link } from "react-router-dom";
function SideBar({ method_list, active_method}) {
    return (
        <aside className="w-1/6 h-screen flex flex-col p-4 pl-6 border-r-2 border-dotted border-[#c2c2c2]">
            <Link to="/" className="text-3xl w-full h-fit flex items-center pb-1 mt-4 mb-3 text-[#00509d]">Calculadoras</Link>
            {
                method_list.map((m) => (
                    <li className={`mb-2 ${m[0] === active_method ? "text-[#00509d] translate-x-3": "hover:text-[#00509d] hover:translate-x-3"} transition ease-out hover:translate-x-3`}>
                        <Link to={`/${m[1]}`} className="text-xl w-full h-10">{m[0]}</Link>
                    </li>
                ))
            }
        </aside>
    )
}


export default SideBar;
