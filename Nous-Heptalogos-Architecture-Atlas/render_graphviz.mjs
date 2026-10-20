// Optional Graphviz WASM driver. The module path is supplied explicitly by the build command.
import {pathToFileURL} from 'node:url';
import path from 'node:path';
const {instance}=await import(pathToFileURL(path.resolve(process.argv[2])).href);
const viz=await instance();
let source='';for await(const chunk of process.stdin)source+=chunk;
process.stdout.write(viz.renderString(source,{format:'svg',engine:'dot'}));
