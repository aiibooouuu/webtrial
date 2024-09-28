// import * as THREE from 'three';
// import { useRef, useReducer, useMemo, useEffect, useState } from 'react';
// import { Canvas, useFrame, useThree } from '@react-three/fiber';
// import { Environment, Lightformer } from '@react-three/drei';
// import { BallCollider, Physics, RigidBody } from '@react-three/rapier';
// import { EffectComposer, RenderPass, EffectPass, BloomEffect, ToneMappingEffect, FXAAEffect } from 'postprocessing';
// import { SSGIEffect, VelocityDepthNormalPass } from './realism-effects/v2';
// import { easing } from 'maath';
// import './app.css';

// // Effects function
// function Effects() {
//   const gl = useThree((state) => state.gl);
//   const scene = useThree((state) => state.scene);
//   const camera = useThree((state) => state.camera);
//   const size = useThree((state) => state.size);
//   const [composer] = useState(() => new EffectComposer(gl, { multisampling: 0 }));

//   useEffect(() => composer.setSize(size.width, size.height), [composer, size]);

//   useEffect(() => {
//     const config = {
//       importanceSampling: true,
//       steps: 20,
//       refineSteps: 4,
//       spp: 1,
//       resolutionScale: 1,
//       missedRays: false,
//       distance: 5.98,
//       thickness: 2.83,
//       denoiseIterations: 1,
//       denoiseKernel: 3,
//       denoiseDiffuse: 25,
//       denoiseSpecular: 25.54,
//       radius: 11,
//       phi: 0.576,
//       lumaPhi: 20.65,
//       depthPhi: 23.37,
//       normalPhi: 26.09,
//       roughnessPhi: 18.47,
//       specularPhi: 7.1,
//       envBlur: 0.8,
//     };

//     const renderPass = new RenderPass(scene, camera);
//     const velocityDepthNormalPass = new VelocityDepthNormalPass(scene, camera);
//     composer.addPass(renderPass);
//     composer.addPass(velocityDepthNormalPass);
//     composer.addPass(
//       new EffectPass(camera, new SSGIEffect(composer, scene, camera, { ...config, velocityDepthNormalPass }))
//     );
//     composer.addPass(
//       new EffectPass(camera, new BloomEffect({ mipmapBlur: true, luminanceThreshold: 0.1, intensity: 0.9, levels: 7 }))
//     );
//     composer.addPass(new EffectPass(camera, new FXAAEffect(), new ToneMappingEffect()));

//     return () => {
//       composer.removeAllPasses();
//     };
//   }, [composer, camera, scene]);

//   useFrame((state, delta) => {
//     gl.autoClear = true;
//     composer.render(delta);
//   }, 1);
// }

// // App Component
// const accents = ['#ff4060', '#ffcc00', '#20ffa0', '#4060ff'];
// const shuffle = (accent = 0) => [
//   { color: '#444', roughness: 0.1, metalness: 0.5 },
//   { color: '#444', roughness: 0.1, metalness: 0.5 },
//   { color: '#444', roughness: 0.1, metalness: 0.5 },
//   { color: 'white', roughness: 0.1, metalness: 0.1 },
//   { color: 'white', roughness: 0.1, metalness: 0.1 },
//   { color: 'white', roughness: 0.1, metalness: 0.1 },
//   { color: accents[accent], roughness: 0.1, accent: true },
//   { color: accents[accent], roughness: 0.1, accent: true },
//   { color: accents[accent], roughness: 0.1, accent: true },
//   { color: '#444', roughness: 0.1 },
//   { color: '#444', roughness: 0.3 },
//   { color: '#444', roughness: 0.3 },
//   { color: 'white', roughness: 0.1 },
//   { color: 'white', roughness: 0.2 },
//   { color: 'white', roughness: 0.1 },
//   { color: accents[accent], roughness: 0.1, accent: true, transparent: true, opacity: 0.5 },
//   { color: accents[accent], roughness: 0.3, accent: true },
//   { color: accents[accent], roughness: 0.1, accent: true },
// ];

// function App() {
//   const [accent, click] = useReducer((state) => ++state % accents.length, 0);
//   const connectors = useMemo(() => shuffle(accent), [accent]);

//   return (
//     <Canvas
//       flat
//       shadows
//       onClick={click}
//       dpr={[1, 1.5]}
//       gl={{ antialias: false }}
//       camera={{ position: [0, 0, 30], fov: 17.5, near: 10, far: 40 }}
//     >
//       <color attach="background" args={['#141622']} />
//       <Physics gravity={[0, 0, 0]}>
//         <Pointer />
//         {connectors.map((props, i) => (
//           <Sphere key={i} {...props} />
//         ))}
//       </Physics>
//       <Environment resolution={256}>
//         <group rotation={[-Math.PI / 3, 0, 1]}>
//           <Lightformer form="circle" intensity={100} rotation-x={Math.PI / 2} position={[0, 5, -9]} scale={2} />
//           <Lightformer form="circle" intensity={2} rotation-y={Math.PI / 2} position={[-5, 1, -1]} scale={2} />
//           <Lightformer form="circle" intensity={2} rotation-y={Math.PI / 2} position={[-5, -1, -1]} scale={2} />
//           <Lightformer form="circle" intensity={2} rotation-y={-Math.PI / 2} position={[10, 1, 0]} scale={8} />
//           <Lightformer form="ring" color="#4060ff" intensity={80} onUpdate={(self) => self.lookAt(0, 0, 0)} position={[10, 10, 0]} scale={10} />
//         </group>
//       </Environment>
//       <Effects />
//     </Canvas>
//   );
// }

// function Sphere({ position, vec = new THREE.Vector3(), r = THREE.MathUtils.randFloatSpread, color = 'white', ...props }) {
//   const api = useRef();
//   const ref = useRef();
//   const pos = useMemo(() => position || [r(10), r(10), r(10)], []);

//   useFrame((state, delta) => {
//     delta = Math.min(0.1, delta);
//     api.current?.applyImpulse(vec.copy(api.current.translation()).negate().multiplyScalar(0.2));
//     easing.dampC(ref.current.material.color, color, 0.2, delta);
//   });

//   return (
//     <RigidBody linearDamping={4} angularDamping={1} friction={0.1} position={pos} ref={api} colliders={false}>
//       <BallCollider args={[1]} />
//       <mesh ref={ref} castShadow receiveShadow>
//         <sphereGeometry args={[1, 64, 64]} />
//         <meshStandardMaterial {...props} />
//       </mesh>
//     </RigidBody>
//   );
// }

// function Pointer() {
//   const ref = useRef();
//   useFrame(({ mouse, viewport }) => ref.current?.setNextKinematicTranslation(new THREE.Vector3((mouse.x * viewport.width) / 2, (mouse.y * viewport.height) / 2, 0)));
//   return (
//     <RigidBody position={[0, 0, 0]} type="kinematicPosition" colliders={false} ref={ref}>
//       <BallCollider args={[1]} />
//     </RigidBody>
//   );
// }

// // Export the App component
// export default App;
import * as THREE from 'three';
import { useRef, useReducer, useMemo, useEffect, useState } from 'react';
import { Canvas, useFrame, useThree } from '@react-three/fiber';
import { Environment, Lightformer, Text } from '@react-three/drei'; // Import Text for static text
import { BallCollider, Physics, RigidBody } from '@react-three/rapier';
import { EffectComposer, RenderPass, EffectPass, BloomEffect, ToneMappingEffect, FXAAEffect } from 'postprocessing';
import { SSGIEffect, VelocityDepthNormalPass } from './realism-effects/v2';
import { easing } from 'maath';
import './app.css';

// Effects function for postprocessing effects
function Effects() {
  const gl = useThree((state) => state.gl);
  const scene = useThree((state) => state.scene);
  const camera = useThree((state) => state.camera);
  const size = useThree((state) => state.size);
  const [composer] = useState(() => new EffectComposer(gl, { multisampling: 0 }));

  useEffect(() => composer.setSize(size.width, size.height), [composer, size]);

  useEffect(() => {
    const config = {
      importanceSampling: true,
      steps: 20,
      refineSteps: 4,
      spp: 1,
      resolutionScale: 1,
      missedRays: false,
      distance: 5.98,
      thickness: 2.83,
      denoiseIterations: 1,
      denoiseKernel: 3,
      denoiseDiffuse: 25,
      denoiseSpecular: 25.54,
      radius: 11,
      phi: 0.576,
      lumaPhi: 20.65,
      depthPhi: 23.37,
      normalPhi: 26.09,
      roughnessPhi: 18.47,
      specularPhi: 7.1,
      envBlur: 0.8,
    };

    const renderPass = new RenderPass(scene, camera);
    const velocityDepthNormalPass = new VelocityDepthNormalPass(scene, camera);
    composer.addPass(renderPass);
    composer.addPass(velocityDepthNormalPass);
    composer.addPass(
      new EffectPass(camera, new SSGIEffect(composer, scene, camera, { ...config, velocityDepthNormalPass }))
    );
    composer.addPass(
      new EffectPass(camera, new BloomEffect({ mipmapBlur: true, luminanceThreshold: 0.1, intensity: 0.9, levels: 7 }))
    );
    composer.addPass(new EffectPass(camera, new FXAAEffect(), new ToneMappingEffect()));

    return () => {
      composer.removeAllPasses();
    };
  }, [composer, camera, scene]);

  useFrame((state, delta) => {
    gl.autoClear = true;
    composer.render(delta);
  }, 1);
}

// Shuffle and manage colors for the hexagons
const accents = ['#ff4060', '#ffcc00', '#20ffa0', '#4060ff'];
const shuffle = (accent = 0) => [
  { color: '#444', roughness: 0.1, metalness: 0.5 },
  { color: '#444', roughness: 0.1, metalness: 0.5 },
  { color: '#444', roughness: 0.1, metalness: 0.5 },
  { color: 'white', roughness: 0.1, metalness: 0.1 },
  { color: 'white', roughness: 0.1, metalness: 0.1 },
  { color: 'white', roughness: 0.1, metalness: 0.1 },
  { color: accents[accent], roughness: 0.1, accent: true },
  { color: accents[accent], roughness: 0.1, accent: true },
  { color: accents[accent], roughness: 0.1, accent: true },
  { color: '#444', roughness: 0.1 },
  { color: '#444', roughness: 0.3 },
  { color: '#444', roughness: 0.3 },
  { color: 'white', roughness: 0.1 },
  { color: 'white', roughness: 0.2 },
  { color: 'white', roughness: 0.1 },
  { color: accents[accent], roughness: 0.1, accent: true, transparent: true, opacity: 0.5 },
  { color: accents[accent], roughness: 0.3, accent: true },
  { color: accents[accent], roughness: 0.1, accent: true },
];
// App component that sets up the 3D environment with hexagons and static text
function App() {
  const [accent, click] = useReducer((state) => ++state % accents.length, 0);
  const connectors = useMemo(() => shuffle(accent), [accent]);

  return (
    <Canvas
      flat
      shadows
      onClick={click}
      dpr={[1, 1.5]}
      gl={{ antialias: false }}
      camera={{ position: [0, 0, 30], fov: 17.5, near: 10, far: 40 }}
    >
      <color attach="background" args={['#141622']} />
      <Physics gravity={[0, 0, 0]}>
        <Pointer />
        {connectors.map((props, i) => (
          <Hexagon key={i} {...props} />
        ))}

        {/* Static Text with Physics */}
        <RigidBody type="fixed" colliders="cuboid">
          <Text
            position={[0, 0, 0]} // Centered text
            fontSize={1.5}
            color="#4060ff" // Opaque black text
            anchorX="center"
            anchorY="middle"
          >
            TICK MY WAY
          </Text>
        </RigidBody>
      </Physics>

      <Environment resolution={256}>
        <group rotation={[-Math.PI / 3, 0, 1]}>
          <Lightformer form="circle" intensity={100} rotation-x={Math.PI / 2} position={[0, 5, -9]} scale={2} />
          <Lightformer form="circle" intensity={2} rotation-y={Math.PI / 2} position={[-5, 1, -1]} scale={2} />
          <Lightformer form="circle" intensity={2} rotation-y={Math.PI / 2} position={[-5, -1, -1]} scale={2} />
          <Lightformer form="circle" intensity={2} rotation-y={-Math.PI / 2} position={[10, 1, 0]} scale={8} />
          <Lightformer
            form="ring"
            color="#4060ff"
            intensity={80}
            onUpdate={(self) => self.lookAt(0, 0, 0)}
            position={[10, 10, 0]}
            scale={10}
          />
        </group>
      </Environment>
      <Effects />
    </Canvas>
  );
}


// App component that sets up the 3D environment with hexagons and static text
// function App() {
//   const [accent, click] = useReducer((state) => ++state % accents.length, 0);
//   const connectors = useMemo(() => shuffle(accent), [accent]);

//   return (
//     <Canvas
//       flat
//       shadows
//       onClick={click}
//       dpr={[1, 1.5]}
//       gl={{ antialias: false }}
//       camera={{ position: [0, 0, 30], fov: 17.5, near: 10, far: 40 }}
//     >
//       <color attach="background" args={['#141622']} />
//       <Physics gravity={[0,0,0]}>
//         <Pointer />
//         {connectors.map((props, i) => (
//           <Hexagon key={i} {...props} />
//         ))}
//       </Physics>
//       <Environment resolution={256}>
//         <group rotation={[-Math.PI / 3, 0, 1]}>
//           <Lightformer form="circle" intensity={100} rotation-x={Math.PI / 2} position={[0, 5, -9]} scale={2} />
//           <Lightformer form="circle" intensity={2} rotation-y={Math.PI / 2} position={[-5, 1, -1]} scale={2} />
//           <Lightformer form="circle" intensity={2} rotation-y={Math.PI / 2} position={[-5, -1, -1]} scale={2} />
//           <Lightformer form="circle" intensity={2} rotation-y={-Math.PI / 2} position={[10, 1, 0]} scale={8} />
//           <Lightformer form="ring" color="#4060ff" intensity={80} onUpdate={(self) => self.lookAt(0, 0, 0)} position={[10, 10, 0]} scale={10} />
//         </group>
//       </Environment>
//       <Effects />
//       {/* Static Text Component */}
//       <Text
//         position={[0, 0, 0]} // Centered text
//         fontSize={1.5}
//         color="#000000" // White text
//         anchorX="center"
//         anchorY="middle"
//       >
//         TICK MY WAY
//       </Text>
//     </Canvas>
//   );
// }

// Hexagon component replacing the Sphere component
function Hexagon({ position, vec = new THREE.Vector3(), r = THREE.MathUtils.randFloatSpread, color = 'white', ...props }) {
  const api = useRef();
  const ref = useRef();
  const pos = useMemo(() => position || [r(10), r(10), r(10)], []);

  useFrame((state, delta) => {
    delta = Math.min(0.1, delta);
    api.current?.applyImpulse(vec.copy(api.current.translation()).negate().multiplyScalar(0.2));
    easing.dampC(ref.current.material.color, color, 0.2, delta);
  });

  return (
    <RigidBody linearDamping={4} angularDamping={1} friction={0.1} position={pos} ref={api} colliders={false}>
      <BallCollider args={[1]} />
      <mesh ref={ref} castShadow receiveShadow>
        {/* Cylinder geometry to represent hexagons */}
        <cylinderGeometry args={[1, 1, 0.5, 6]} /> {/* 6 sides for hexagon */}
        <meshStandardMaterial {...props} />
      </mesh>
    </RigidBody>
  );
}

// Pointer component for interaction
function Pointer() {
  const ref = useRef();
  useFrame(({ mouse, viewport }) =>
    ref.current?.setNextKinematicTranslation(
      new THREE.Vector3((mouse.x * viewport.width) / 2, (mouse.y * viewport.height) / 2, 0)
    )
  );
  return (
    <RigidBody position={[0, 0, 0]} type="kinematicPosition" colliders={false} ref={ref}>
      <BallCollider args={[1]} />
    </RigidBody>
  );
}

// Export the App component
export default App;
