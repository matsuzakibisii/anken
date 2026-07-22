/* ANKEN 本体サイト – Tailwind デザイントークン共通設定
   index.html / member.html / contact.html から読み込む。
   カラー・フォント等のデザインガイドラインを変更する場合はこのファイルのみ編集する。
   （<script src="https://cdn.tailwindcss.com"></script> の直後に読み込むこと） */
tailwind.config = {
  theme: {
    extend: {
      colors: {
        ink: '#0B1221',
        midnight: '#101935',
        accent: '#F59E0B',
        accentDark: '#B45309',
        accentText: '#92400E',
        highlight: '#FACC15',
        softgray: '#FAF8F2',
      },
      fontFamily: {
        sans: ['"Noto Sans JP"', '"Hiragino Kaku Gothic ProN"', 'system-ui', 'sans-serif'],
      },
    },
  },
};
