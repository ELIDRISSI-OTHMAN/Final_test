[Setup]
AppId={{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}
AppName=Tissue Fragment Stitching Tool
AppVersion=1.0.1
AppVerName=Tissue Fragment Stitching Tool 1.0.1
AppPublisher=Scientific Imaging Lab
AppPublisherURL=https://github.com/scientific-imaging/tissue-stitcher
AppSupportURL=https://github.com/scientific-imaging/tissue-stitcher/issues
AppUpdatesURL=https://github.com/scientific-imaging/tissue-stitcher/releases
DefaultDirName={autopf}\TissueStitcher
DefaultGroupName=Tissue Fragment Stitching Tool
AllowNoIcons=yes
LicenseFile=LICENSE
InfoBeforeFile=SYSTEM_REQUIREMENTS.txt
OutputDir=installer
OutputBaseFilename=TissueStitcher-Setup-v1.0.1
SetupIconFile=icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
MinVersion=10.0
UninstallDisplayIcon={app}\TissueStitcher.exe
UninstallDisplayName=Tissue Fragment Stitching Tool
VersionInfoVersion=1.0.1
VersionInfoCompany=Scientific Imaging Lab
VersionInfoDescription=Professional tool for tissue fragment arrangement and stitching
VersionInfoCopyright=Copyright (C) 2024 Scientific Imaging Lab

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
Source: "SYSTEM_REQUIREMENTS.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "USER_GUIDE.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "LICENSE"; DestDir: "{app}"; Flags: ignoreversion
; Icon file (if exists)
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion skipifsourcedoesntexist

[Icons]
Name: "{group}\Tissue Fragment Stitching Tool"; Filename: "{app}\TissueStitcher.exe"
Name: "{group}\User Guide"; Filename: "{app}\USER_GUIDE.txt"
Name: "{group}\System Requirements"; Filename: "{app}\SYSTEM_REQUIREMENTS.txt"
Name: "{group}\{cm:ProgramOnTheWeb,Tissue Fragment Stitching Tool}"; Filename: "https://github.com/scientific-imaging/tissue-stitcher"
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