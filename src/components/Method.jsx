import React, { useEffect, useState } from "react";
import axios from "axios";
import MethodForm from "./MethodForm";
import Table from "./Table";
function Method({ method_route, method_name }) {
    const [method_data, setMethod_data] = useState({});
    console.log(method_route);
    console.log(method_name);
    
    const get_method = async () => {
        const res = await axios.get(`http://localhost:5000/${method_route}`);
        setMethod_data(res.data);
    }

    const put_method = (input) => {
        axios.post(`http://localhost:5000/${method_route}`, { input })
            .then(res => console.log(res)).catch(err => console.log(error));
    }

    useEffect(() => {
        get_method();
    }, [])


    return (
        <main className="w-full h-[76vh] p-6">
            <h1 className="w-fit text-start text-5xl mb-3 text-[#00509d]">
                {method_name}
            </h1>
            <h2 className="text-2xl text-gray-500 text-opacity-100">Explicación</h2>
            <p className="mt-3 border-b-2 border-dotted pb-6 w-fit text-justify">
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aspernatur suscipit corporis, fugit ad nulla reiciendis quaerat expedita similique culpa necessitatibus, inventore doloremque labore illum, commodi incidunt qui excepturi iure exercitationem!
                Voluptates aliquid nemo temporibus! Quam, amet aliquid. Tenetur harum consequuntur nostrum vitae omnis excepturi animi magnam facere, eum maxime nihil culpa, reprehenderit illum! Necessitatibus incidunt eum, maxime laboriosam sed cumque?
            </p>
            <h2 className="text-2xl text-gray-500 text-opacity-100 mt-3">Calculadora</h2>
            <section className="w-full h-3/4 flex mt-4 justify-evenly">
                <MethodForm method_name={method_name} method_obj={method_data} put_method={put_method} />
                <Table />
            </section>
        </main>
    );
}


export default Method;