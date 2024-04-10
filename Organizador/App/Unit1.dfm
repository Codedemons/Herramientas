object FrmPrincipal: TFrmPrincipal
  Left = 0
  Top = 0
  Align = alClient
  BorderIcons = []
  BorderStyle = bsNone
  ClientHeight = 480
  ClientWidth = 640
  Color = cl3DLight
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  TextHeight = 15
  object PnlTitulo: TPanel
    Left = 0
    Top = 0
    Width = 640
    Height = 50
    Align = alTop
    Color = clMedGray
    DockSite = True
    ParentBackground = False
    TabOrder = 0
    object ImgClose: TImage
      Left = 591
      Top = 1
      Width = 48
      Height = 48
      Align = alRight
      ExplicitLeft = 1
    end
    object ImgTitle: TImage
      Left = 1
      Top = 1
      Width = 48
      Height = 48
      Align = alLeft
    end
    object ImgMini: TImage
      Left = 543
      Top = 1
      Width = 48
      Height = 48
      Align = alRight
      ExplicitLeft = 1
    end
  end
  object PnlContent: TPanel
    Left = 0
    Top = 50
    Width = 640
    Height = 430
    Align = alClient
    Color = clGray
    ParentBackground = False
    TabOrder = 1
    ExplicitLeft = 280
    ExplicitTop = 272
    ExplicitWidth = 185
    ExplicitHeight = 41
  end
end
