document.addEventListener('DOMContentLoaded', () => {
    // tsParticles initiation
    tsParticles.load("tsparticles", {
        // Use a black background
        background: {
            color: "#000000"
        },
        // Make the animation full screen, covering the container
        fullScreen: {
            enable: true,
            zIndex: -1 // Match our CSS z-index
        },
        // Particle configuration
        particles: {
            // --- The Stars ---
            number: {
                value: 400, // Number of stars
                density: {
                    enable: true,
                    value_area: 800
                }
            },
            color: {
                value: "#ffffff" // Star color
            },
            shape: {
                type: "circle" // Star shape
            },
            opacity: {
                value: {min: 0.1, max: 0.8}, // Give stars random opacity
                animation: {
                    enable: true,
                    speed: 0.5,
                    sync: false
                }
            },
            size: {
                value: { min: 0.5, max: 2 } // Give stars random sizes
            },
            links: {
                enable: false,
            },
            move: {
                enable: true,
                speed: 0.3, // Slow drift
                direction: "none",
                random: true,
                straight: false,
                out_mode: "out",
                bounce: false
            }
        },
        // --- The Meteors ---
        emitters: {
            direction: "top-right",
            // --- THIS IS THE UPDATED SECTION ---
            rate: {
                // Now, the delay is a random value between 5 and 15 seconds
                delay: {
                    min: 1,
                    max: 2
                },
                quantity: 5
            },
            // --- END OF UPDATED SECTION ---
            position: {
                x: 0,
                y: 50
            },
            size: {
                width: 0,
                height: 0
            },
            particles: {
                move: {
                    direction: -45,
                    enable: true,
                    outModes: {
                        default: "destroy"
                    },
                    speed: 20,
                    trail: {
                        enable: true,
                        fillColor: "#000",
                        length: 20
                    },
                },
                opacity: {
                    value: 0
                },
                size: {
                    value: 3
                },
                links: {
                    enable: false
                }
            }
        },
        interactivity: {
            detect_on: "canvas",
            events: {
                onhover: {
                    enable: false,
                },
                onclick: {
                    enable: false,
                },
                resize: true
            }
        },
        detectRetina: true
    });
});