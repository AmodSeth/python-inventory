import { useState } from "react";

// export default function Parent_RandomNumberGenerator_function() {
//   // const [value, setValue] = useState(null);

//   // const generate = () => {
    
//   //   const num = Math.floor(Math.random() * 100) + 1;
//   //   setValue(num);
//   // };

//   // return (
//   //   <div style={{ textAlign: "center", padding: "20px" }}>
//   //     <h2>Random Number</h2>
//   //     <p style={{ fontSize: "2rem", margin: "20px 0" }}>
//   //       {value !== null ? value : "--"}
//   //     </p>
//   //     <button
//   //       onClick={generate}
//   //       style={{
//   //         padding: "10px 20px",
//   //         fontSize: "1rem",
//   //         borderRadius: "8px",
//   //         cursor: "pointer",
//   //       }}
//   //     >
//   //       Generate
//   //     </button>
//   //   </div>
//   );
// }



export default function Parent_RandomNumberGenerator_function({ value, setValue }) {
  return (
    <div>
      <NumberGenerator onGenerate={setValue} />
      <DisplayNumber number={value} />
    </div>
  );
}



function NumberGenerator({onGenerate} ) {    
  // i need a function to genrate the number with that fuckting button

  const generate = () => {
    const num = Math.floor(Math.random() * 100) + 1;
    onGenerate(num);
  };

  return (
    <button onClick={generate}>
      Generate Number 
    </button>
  )

}

function DisplayNumber({number}){
    return (
        <div>
            <h2>Random Number</h2>
            <p style={{ fontSize: "2rem", margin: "20px 0" }}>
              {number !== null ? number : "--"}
            </p>
        </div>
    )
}