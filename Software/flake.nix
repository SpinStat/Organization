{
  description = "Development environment for TI AM62 Yocto & FreeRTOS";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }: 
    let 
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in {
      devShells.x86_64-linux.default = pkgs.mkShell {
        name = "am62-dev";

        # Packages for Yocto & QEMU Development
        buildInputs = with pkgs; [
          git
          direnv
          nixFlakes
          qemu
          gdb-multiarch
          python3
          cmake
          ninja
          ccache
          clang-tools
          meson
          flex
          bison
          dtc  # Device tree compiler
          ubootTools  # mkimage for U-Boot
          cpio  # Needed for building initramfs
          rsync  # For syncing build outputs
        ];

        # Cross-Compilers for ARM & Cortex-M
        nativeBuildInputs = with pkgs; [
          gcc-arm-embedded  # GCC toolchain for Cortex-M
          gcc-aarch64-none-elf  # GCC toolchain for Cortex-A
        ];

        # Environment variables
        shellHook = ''
          export CROSS_COMPILE=aarch64-none-elf-
          export ARCH=arm64
          export PATH=$PWD/build/bin:$PATH
          echo "Welcome to the AM62 Yocto & FreeRTOS Dev Environment!"
        '';
      };
    };
}

