import discord
from discord.ext import commands

class ServStatus(commands.Cog):
      def __init__(self, bot):
            self.bot = bot
            
      @commands.command(aliases=["aaa"])
      async def aa(self, ctx):
            """aaaa"""
            embed=discord.Embed(title="Come installare RiiConnect24 sulla Wii", description="*Guida scritta da wii.guide, riscritta da Vincysuper07*", color=0x00ff00)
            embed.set_author(name="Vincysuper07")
            embed.add_field(name="Requisiti:", value="1. Una Wii connessa a Internet\n2. Una scheda SD\n3. Un PC Windows (il programma per Mac/Linux ancora non funziona)\n4. Il patcher di RiiConnect24", inline=True)
            embed.add_field(name="Link utili (clicca per scaricare):", value="[RiiConnect24 Patcher](https://github.com/RiiConnect24/RiiConnect24-Patcher/releases/download/v1.1.2.3/RiiConnect24Patcher.bat)\n[Applicazioni già patchate (Wii ver 4.3E) per chi non ha il computer Windows](http://uploadgram.gq/f/ITY.zip)", inline=True)
            embed.add_field(name="Iniziamo!", value="1. Inserire la SD nel PC\n2. Scaricate e aprite il RiiConnect24 Patcher dal link di sopra\n•Se non hai un PC Windows, scaricate il file zip dal link di sopra e mettete il contenuto nella SD\n3. Dal menù che dovrebbe uscire premere 1 e poi premere invio\n4. Premere 1 per installare riiconnect24 sulla propria wii e premere invio, poi premere 1 di nuovo per installare tutti i canali\n5. Scegliere la regione della console (se la versione della Wii è 4.3E, premere 1) e poi premere invio\n6. Se avete collegato la vostra scheda SD al computer, premete 1 altrimenti premete 2, e poi premere invio\n7. Premere 1 per iniziare a patchare\n•Questo potrebbe richiedere un po' di tempo a seconda del processore o della connessione\n8. Collegare la SD alla Wii\n•Se avete usato la seconda opzione, andare nella cartella dove avete messo il patcher e cercate la cartelle “WAD” e “apps” e copiarle quando potete\nEcco i passaggi su Wii:\n9. Aprite Homebrew Channel\n10. Aprire “Wii Mod Lite” e andare su “WAD Manager”\n11. Premere + sui wad “Everybody Votes Channel”, “Mii Contest Channel”, “Nintendo Channel”, “IOS31”, “IOS80” e premere A per installare tutto\n12. A fine installazione, premere HOME per tornare a Homebrew Channel\n13. Aprire “RiiConnect24 Mail Patcher” e premere HOME quando ||se|| ve lo chiede\n14. Andare nelle Impostazioni della Wii>Internet\n15. Andare nella connessione che state utilizzando>Cambia impostazioni\n16. Cambiare “Ottieni automaticamente DNS” su “No” e poi cliccare su “Opzioni Avanzate”\n17. Impostare il DNS primario a `164.132.44.106` e il DNS secondario a `8.8.8.8`\n18. Salvare le impostazioni, fare la prova di connessione e, se si connette, cliccare su “No” per saltare l'aggiornamento\n19. Torna indietro (sempre nelle impostazioni Internet) e cliccare su “Accordo/Contatto”, cliccare su “Si” e accettare i termini di servizio di RiiConnect24", inline=False)
            embed.add_field(name="Ultima cosa", value="Se è andato tutto bene, potrete trovare degli altri canali sul menu Wii\nPer testare, andare sul Canale Meteo o Canale Notizie, se non danno nessun errore, significa che RiiConnect24 è stato installato con successo!", inline=False)
            embed.set_footer(text="Buon divertimento!")
            await ctx.send(embed=embed)
            
def setup(bot):
      bot.add_cog(ServStatus(bot))
