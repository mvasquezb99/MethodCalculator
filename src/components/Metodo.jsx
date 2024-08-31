import React, { useEffect, useState } from "react";
import axios from "axios";
function Metodo({ method_name }) {
    const [method_data, setMethod_data] = useState({});

    const get_method = async () => {
        const res = await axios.get(`http://localhost:5000/${method_name}`);
        setMethod_data(res.data);
    }

    useEffect(() => {
        get_method();
    },[])

    const { E: Errors, Xm, fxm } = method_data;

    return (
        <main className="w-full h-screen">
            <h1 className="w-full text-center text-2xl">
                {method_name}
            </h1>
        </main>
    );
}


export default Metodo;