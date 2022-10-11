<h1 align="center">EMG Feature Extraction Toolkit</h1>

The goal of this toolkit is to provide an easy to use API for EMG feature extraction. This is an open sourced toolkit developed at the University of New Brunswick by lab members at the Institute of Biomedical Engineering.

Authors: Ethan Eddy, Evan Campbell and Erik Scheme

## Overview

- [Features](#features)
- [Documentation](#documentation)
- [Example](#example)
- [Rerences](#references)

## Features

Let $x_{i}$ represents the signal in segment i and $N$ denotes the number of samples in the timeseries.

#### **Mean Absolute Value (MAV)**
The average of the absolute value of the EMG signal. This is one of the most commonly used features for EMG.
```math
    \text{MAV} = \sum_{i=1}^{N} |x_{i}|
```

#### **Zero Crossings (ZC)**
The number of times that the amplitude of the EMG signal crosses a zero amplitude threshold. The goal of this feature is to avoid low-level voltage fluctuations and background noise. 
```math
    \text{ZC} = \sum_{i=1}^{N-1}[\text{sgn}(x_{i} \times x_{i+1}) \cap |x_{i} - x_{i+1}| \ge \text{threshold}] 
```
```math
    \text{sgn(}x\text{)} = \left\{\begin{array}{lr}
        1, & \text{if } x \ge \text{threshold} \\
        0, & \text{otherwise }
        \end{array}\right\}
```

#### **Slope Sign Change (SSC)**
The number of times that the slope of the EMG signal changes (i.e., the number of times that it changes between positive and negative). This is used to help eliminate background noise.
```math
    \text{SSC} = \sum_{i=2}^{N-1}[f[(x_{i} - x_{i-1}) \times (x_{i} - x_{i+1})]] \\
```
```math
    f(x) = \left\{\begin{array}{lr}
        1, & \text{if } x \ge \text{threshold} \\
        0, & \text{otherwise }
        \end{array}\right\}
```

#### **Waveform Length (WL)**
The cumulative length of the EMG waveform over the passed in window. This feature is used to measure the overall complexity of the signal (i.e., higher WL means more complex).
```math
    \text{WL} = \sum_{i=1}^{N-1}|x_{i+1} - x_{i}|
```

#### **? (LS)**

#### **? (MFL)**

#### **? (MSR)**

#### **Willison Amplitude (WAMP)**
The number of times that there is a difference between amplitudes of two seperate samples exceeding a pre-defined threshold. This feature is related to the firing of motor unit action potentials and muscle contraction force.
```math
    \text{WAMP} = \sum_{i=1}^{N-1}[f(|x_{n}-x_{n+1})] \\
```
```math    
    f(x) = \left\{\begin{array}{lr}
        1, & \text{if } x \ge \text{threshold} \\
        0, & \text{otherwise }
        \end{array}\right\}
```

#### **Root Mean Square (RMS)**
```math
    \text{RMS} = \sqrt{\frac{1}{N}\sum_{i=1}^{N}x_{i}^{2}}
```

#### **? (IAV)**

#### **? (DASDV)**

#### **Variance (VAR)**
```math
    \text{VAR} = \frac{1}{N-1}\sum_{i=1}^{N} x_{i}^{2}
```

#### **? (M0)**

#### **? (M2)**

#### **? (M4)**

#### **? (SPARSI)**

#### **? (IRF)**

#### **? (WLF)**

#### **? (AR)**

#### **? (CC)**

#### **? (LD)**

#### **? (MAVFD)**

#### **? (MAVSLP)**

#### **? (MDF)**

#### **? (MNF)**

#### **? (MNP)**

#### **? (MPK)**

#### **? (SAMPEN)**

#### **? (SKEW)**

#### **? (KURT)**

## Documentation

## Example

## References

```
Angkoon Phinyomark, Pornchai Phukpattaranont, Chusak Limsakul,
Feature reduction and selection for EMG signal classification,
Expert Systems with Applications,
Volume 39, Issue 8,
2012,
Pages 7420-7431,
ISSN 0957-4174,
https://doi.org/10.1016/j.eswa.2012.01.102.
(https://www.sciencedirect.com/science/article/pii/S0957417412001200)
```