[Setup]
AppId={{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}
AppName=Tissue Fragment Stitching Tool
AppVersion=1.0.0
AppVerName=Tissue Fragment Stitching Tool 1.0.0
AppPublisher=Scientific Imaging Lab
AppPublisherURL=https://github.com/your-repo
AppSupportURL=https://github.com/your-repo/issues
AppUpdatesURL=https://github.com/your-repo/releases
DefaultDirName={autopf}\TissueStitcher
DefaultGroupName=Tissue Fragment Stitching Tool
AllowNoIcons=yes
LicenseFile=LICENSE
InfoBeforeFile=README.md
OutputDir=installer
OutputBaseFilename=TissueStitcher-Setup-v1.0.0
SetupIconFile=icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1

[Files]
; Main application files
Source: "dist\TissueStitcher\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; Documentation
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "LICENSE"; DestDir: "{app}"; Flags: ignoreversion
; Icon file (if exists)
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion; Check: FileExists(ExpandConstant('{srcexe}\..\icon.ico'))

[Icons]
Name: "{group}\Tissue Fragment Stitching Tool"; Filename: "{app}\TissueStitcher.exe"
Name: "{group}\{cm:ProgramOnTheWeb,Tissue Fragment Stitching Tool}"; Filename: "https://github.com/your-repo"
Name: "{group}\{cm:UninstallProgram,Tissue Fragment Stitching Tool}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Tissue Fragment Stitching Tool"; Filename: "{app}\TissueStitcher.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Tissue Fragment Stitching Tool"; Filename: "{app}\TissueStitcher.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\TissueStitcher.exe"; Description: "{cm:LaunchProgram,Tissue Fragment Stitching Tool}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"

[Code]
function FileExists(FileName: string): Boolean;
begin
  Result := FileExists(FileName);
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    // Add any post-install tasks here
  end;
end;