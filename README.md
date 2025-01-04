# Evolvium

Evolvium is an open-source evolution simulator that demonstrates natural selection, population dynamics, and emergent behaviors in complex systems. Built in Python and visualized using Pygame, Evolvium creates an environment where digital organisms compete, evolve, and adapt.

## Features

- **Real-time Visualization**: Watch evolution happen before your eyes with a color-coded grid system
- **Complex Cell Types**: Multiple specialized cells that form organism behaviors
- **Natural Selection**: Organisms compete for resources and evolve through reproduction and mutation
- **Emergent Behaviors**: Watch as organisms develop different survival strategies!

## Installation

1. Clone the repository:
```bash
git clone https://github.com/matanitah/evolvium.git
cd evolvium
```

2. Install dependencies:
```bash
pip install pygame numpy
```

## Usage

Run the simulation:
```bash
python main.py
```

## Cell Types

### Independent Cells
- **Empty** (Dark Blue): Inert cells that can be occupied
- **Food** (Grayish-Blue): Provides nourishment for organisms
- **Wall** (Gray): Blocks organism movement and reproduction

### Organism Cells
- **Mouth** (Orange): Consumes food from adjacent cells
- **Producer** (Green): Generates food in adjacent empty cells
- **Mover** (Light Blue): Enables organism movement and rotation
- **Killer** (Red): Damages adjacent organisms
- **Armor** (Purple): Protects against killer cells
- **Builder** (Brown): Constructs walls in adjacent empty cells

## Organism Behavior

### Movement
- Organisms with mover cells can move in any direction
- Movement preserves organism structure
- Collisions with walls and other organisms are prevented
- Movement costs energy

### Feeding
- Mouth cells consume adjacent food
- Each food piece provides energy
- Food consumption is tracked for reproduction

### Reproduction
- Occurs when food eaten equals organism cell count
- Offspring spawns at a safe distance from parent
- Three possible mutations during reproduction:
  - Change: Random cell becomes a different type
  - Lose: Random cell is removed
  - Add: New cell grows adjacent to existing one

## Energy System
- Organisms consume energy based on size
- Movement costs additional energy
- Energy gained through food consumption
- Death occurs at zero energy

## Configuration

Edit `config/settings.py` to modify:
- Grid dimensions
- Cell size
- Simulation speed
- Color schemes
- Initial conditions

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - [Matan Itah](https://linkedin.com/matanitah)
Project Link: [https://github.com/matanitah/evolvium](https://github.com/matanitah/evolvium)