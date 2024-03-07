# ARQUITECTURE_SOLIDPROJECT
En una era donde la tecnología redefine constantemente las expectativas de los consumidores, una empresa emergente visionaria se embarcó en una misión para revolucionar la forma en que las personas interactúan con y aprovechan sus múltiples beneficios financieros y de servicios. Inspirados por la complejidad que enfrentaban los usuarios al gestionar sus beneficios dispersos en seguros, tarjetas de crédito, y programas de fidelización, el equipo se propuso construir un sistema unificado que no solo centralizara estos beneficios en una sola plataforma, sino que también orientara a los usuarios hacia la maximización de su valor en cada compra. Este sistema integrado de beneficios se convirtió en la piedra angular de su visión, prometiendo una interfaz intuitiva respaldada por una arquitectura robusta y un motor de recomendaciones inteligente.

Al abordar el diseño del sistema, la elección de una arquitectura de microservicios emergió como la solución óptima, promoviendo la flexibilidad, la escalabilidad y la facilidad de integración con sistemas externos. Esta arquitectura facilitaría la actualización y expansión continuas del sistema, permitiendo al equipo añadir nuevos proveedores de beneficios o actualizar los existentes sin interrupciones significativas.

Por otra parte, la identificación de los requerimientos críticos, equilibrando cuidadosamente las necesidades funcionales, como la integración transparente con diversos proveedores de beneficios y un sistema de recomendaciones altamente personalizado, con imperativos no funcionales como seguridad de datos, escalabilidad y disponibilidad. La meta es crear un sistema que no solo respondiera a las necesidades actuales de los usuarios, sino que también pudiera adaptarse a las demandas futuras.

La presentación clara de los beneficios disponibles, junto con una retroalimentación inmediata y relevante sobre las recomendaciones de beneficios, se convirtió en una prioridad para asegurar que los usuarios pudieran tomar decisiones informadas con facilidad. Así mismo, con los cimientos tecnológicos en su lugar, la experiencia del usuario debe ser visualmente atractiva y accesible en una variedad de dispositivos, si no que también proporcionara una interacción intuitiva con el sistema.

La implementación del sistema debe seguir los principios SOLID para asegurar un código mantenible y extensible. Cada microservicio debe ser construido con un propósito específico, desde gestionar la autenticación de usuarios hasta procesar complejas recomendaciones de beneficios. La seguridad fue debe estar en cada etapa empleando las mejores prácticas para proteger la información personal y financiera de los usuarios.

### Principio de responsabilidad única (Single Responsibility Principle)
para este primer principio, encontramos en el desarrollo del proyecto dos clases,  la primera clase usuarios.py y la clase GestionServicios.py mantienen responsabilidad unicas, las cuales contienen responsabilidades especificas como por ejemplo, es el caso de la clase usuarios, dentro de ella se encuentra la creacion y registro de un usurio, y su respectiva validacion en el sistema por medio de un inicio de secion. por otra parte, en la clase GestionServicios, encontramos que es capaz de reunir otras subclases como por ejemplo Serviciosseguro, Servicioprograma y Serviciotargeta.

### Principio de abierto/cerrado (Open/Closed Principle)
para este segundo principio, nos define como las entendidades del software (clases, modulos, funciones, etc) deben estar abiertas para una posible extension, pero cerradas para su modificaciones, en este proyecto, la clase GestionServicios, puede tener la capacidad de estar abierta para una posible extension. es decir por medio de metodos que puedan agregar nuevos servicios sin tener que modificarse las clases ya existentes. 

### Principio de sustitución de Liskov (Liskov Substitution Principle)
para este tercer principio, Los objetos de una clase deben poder ser reemplazados por objetos de una subclase sin afectar la corrección del programa. Para seguir este principio, podrías asegurarte de que cualquier clase que herede de otra pueda ser usada en lugar de la clase padre sin causar problemas. en este ejemplo, no vemos aplicacion de herencia, sin embargo. podremos usar las clases se pueden implementar metodos generales en una clase padre, y estos poderlos adaptar y utilizar en las clases hijas, como por ejemplo la clase GestionServicios. 

### Principio de segregación de la interfaz (Interface Segregation Principle)
para este cuarto principio, Los clientes no deben ser forzados a depender de interfaces que no usan. En este proyecto, la clase GestionServicios proporciona una interfaz simple con solo unos pocos métodos, por lo que parece adherirse al ISP. sin embargo eso no bastaria para lograr una flexivilidad optima. 

### Principio de inversión de dependencia (Dependency Inversion Principle)
Los módulos de alto nivel no deberían depender de los módulos de bajo nivel. Ambos deberían depender de abstracciones. Tu clase GestionServicios depende de las clases concretas Servicioseguro, Serviciotargeta, y Servicioprograma. lo cual es poco para poder seguir los lineamientos de este principio, se podria optimizar si defino las clases base abstractas o interfaces para estos servicios, y hacer asi que GestionServicios dependa de estas abstracciones en lugar de las clases concretas.

## Diagrama de clases 
![arch_2](https://github.com/luisariass/ARQUITECTURE_SOLIDPROJECT/assets/141878301/067b1a8b-c063-4a9c-b1c7-869c36005efa)


