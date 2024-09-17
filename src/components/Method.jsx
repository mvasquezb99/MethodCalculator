import React, { useEffect, useState } from "react";
import axios from "axios";
import MethodForm from "./MethodForm";
import Table from "./Table";
function Method({ method_name }) {
    const [method_data, setMethod_data] = useState({});

    const get_method = async () => {
        const res = await axios.get(`http://localhost:5000/${method_name}`);
        setMethod_data(res.data);
    }

    const put_method =  (input) => {
        axios.post(`http://localhost:5000/${method_name}`,{input})
        .then(res => console.log(res)).catch(err => console.log(error));
    }

    useEffect(() => {
        get_method();
    }, [])


    return (
        <main className="w-full h-[76vh] p-6">
            <h1 className="w-fit text-start text-5xl first-letter:uppercase mb-3">
                {method_name}
            </h1>
            <h2 className="text-2xl text-gray-500 text-opacity-100">Explicación</h2>
            <p className="mt-3 border-b-2 border-dotted pb-6 w-fit text-justify">
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aspernatur suscipit corporis, fugit ad nulla reiciendis quaerat expedita similique culpa necessitatibus, inventore doloremque labore illum, commodi incidunt qui excepturi iure exercitationem!
                Voluptates aliquid nemo temporibus! Quam, amet aliquid. Tenetur harum consequuntur nostrum vitae omnis excepturi animi magnam facere, eum maxime nihil culpa, reprehenderit illum! Necessitatibus incidunt eum, maxime laboriosam sed cumque?
            </p>
            <section className="w-full h-3/4 flex mt-6 justify-evenly">
                <MethodForm method_name={method_name} method_obj={method_data} put_method={put_method}/>
                <Table/>
            </section>
        </main>
    );
}


export default Method;