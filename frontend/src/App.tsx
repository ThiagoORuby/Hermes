import { useState } from "react";

export function App() {
  let [minhaString, setMinhaString] = useState<String>("Thiago");

  return (
    <div>
      <p> Hello, World! {minhaString} </p>
      <p>Nao sei o que fazer aqui</p>
      <button onClick={() => setMinhaString("outrooo")}>meu botao</button>
    </div>
  );
}
