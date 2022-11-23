import React from "react";
import { render } from 'react-dom';
import { ChakraProvider } from "@chakra-ui/react";

import Header from "./components/Header";
import Todos from "./components/Todos";

function App() {
    return (
        <ChakraProvider>
            <Header />
            <Todos />
        </ChakraProvider>
    )
}

const rootElement = document.getElementById("root")
render(<App />, rootElement)
